from typing import TypedDict

from .image import Image


class Album(TypedDict):
    id: str
    name: str
    total_tracks: int
    album_type: str
    available_markets: list[str]
    href: str
    images: list[Image]
    release_date: str
    release_date_precision: str
