import re
from typing import List, Literal

from auth import spotify
from utils.url import url_to_id


def search_by_genre(
    genre: str,
    count: Literal[50, 100, 150] = 150,
) -> List[dict]:
    limit = 50
    playlists = []

    for offset in range(0, count, limit):
        print(offset)
        search = spotify.search(genre, limit, offset, type="playlist")
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
            artists(name),
            album(
                release_date,
                images
            )
        )
    )
""",
)


def get_tracks(playlist_id: str, fields=PLAYLIST_FIELDS):
    offset = 0
    count = 0
    tracks = []

    while True:
        data = spotify.playlist_tracks(playlist_id, fields=fields, offset=offset)
        total = int(data["total"])
        count += len(data["items"])

        tracks.extend(data["items"])

        if total > count:
            matches = re.findall("offset=(\\d+)", data["next"])
            offset = int(matches[0])
        else:
            break

    return tracks


def get_tracks_from_many(playlists: List[dict]) -> List[dict]:
    tracks: List[dict] = []

    for i in range(len(playlists)):
        playlist_id = url_to_id(playlists[i]["href"])
        print(f"playlist #{i + 1} - {playlist_id}")

        playlist_tracks = get_tracks(playlist_id)

        print("tracks count ", len(playlist_tracks))
        tracks.extend(playlist_tracks)

    return [x["track"] for x in tracks if x["track"] is not None]
