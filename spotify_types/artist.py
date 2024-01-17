from typing import TypedDict

from .image import Image


class Artist(TypedDict):
    id: str
    name: str
    href: str
    images: list[Image]
    popularity: int
