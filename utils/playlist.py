import re
from typing import Literal

import utils.track as tr
from auth import spotify
from spotify_types import Playlist, PlaylistItemsResponse, SearchResult, Track
from utils.url import url_to_id


def search_by_genre(
    genre: str,
    count: Literal[50, 100, 150] = 150,
) -> list[Playlist]:
    limit = 50
    playlists: list[Playlist] = []

    for offset in range(0, count, limit):
        search: SearchResult | None = spotify.search(
            q=genre, limit=limit, offset=offset, type="playlist"
        )

        if search is None:
            raise Exception("Error in search request")

        playlists.extend(search["playlists"]["items"])

    return playlists


PLAYLIST_FIELDS = re.sub(
    "(\\n|\\s)",
    "",
    """
    total,
    next,
    items(
        track(
            id,
            name,
            popularity,
            artists(name),
            album(
                release_date,
                images
            )
        )
    )
""",
)


def get_tracks(playlist_id: str, fields=PLAYLIST_FIELDS) -> list[Track]:
    offset, count = 0, 0
    tracks: list[Track] = []

    while True:
        data: PlaylistItemsResponse | None = spotify.playlist_tracks(
            playlist_id, fields=fields, offset=offset
        )

        if data is None:
            raise Exception("Error in playlist_items request")

        total = int(data["total"])
        count += len(data["items"])
        next_url = data["next"]
        # without 'track' key
        # and filtered broken tracks
        cleaned_tracks = [
            x["track"]  # noqa
            for x in data["items"]
            if tr.is_valid(x["track"])
        ]

        tracks.extend(cleaned_tracks)

        if total > count and next_url is not None:
            matches = re.findall("offset=(\\d+)", next_url)
            offset = int(matches[0])
        else:
            break

    return tracks


def get_tracks_from_many(playlists: list[Playlist]) -> list[Track]:
    tracks: list[Track] = []

    for i, playlist in enumerate(playlists):
        playlist_id = url_to_id(playlist["href"])
        print(f"playlist #{i + 1} - {playlist_id}")

        playlist_tracks = get_tracks(playlist_id)

        print("tracks count ", len(playlist_tracks))
        tracks.extend(playlist_tracks)

    return tracks
