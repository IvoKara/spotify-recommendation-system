from typing import Literal, TypedDict

from .basic import ResponseObject
from .image import Image
from .track import Track


class Playlist(TypedDict):
    id: str
    name: str
    collaborative: bool
    description: str | None
    external_urls: dict[Literal["spotify"], str]
    href: str
    images: list[Image]
    owner: dict
    uri: str


class PlaylistItemsResponse(ResponseObject):
    items: list[Track]
