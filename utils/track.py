from typing import TypedDict

from spotify_types import Image, Track


class PreparedTrack(TypedDict):
    track_id: str
    track_name: str
    artists: list[str]
    image_url: str | None
    release_date: str
    popularity: int


def prepare(track: Track) -> PreparedTrack:
    album_images: list[Image] = track["album"]["images"]

    prepared: PreparedTrack = {
        "track_id": track["id"],
        "track_name": track["name"],
        "artists": [artist["name"] for artist in track["artists"]],
        "image_url": album_images[0]["url"] if album_images else None,
        "release_date": track["album"]["release_date"],
        "popularity": track["popularity"] or 0,
    }

    return prepared


def is_valid(track: Track) -> bool:
    # Instruct Ruff to remain it on multiple lines
    return (
        track is not None  # noqa
        and track["id"] is not None
        and track["name"] is not None
    )
