import re
from typing import List, Literal

from auth import spotify


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
