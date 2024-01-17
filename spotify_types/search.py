from typing import TypedDict

from .basic import ResponseObject
from .playlist import Playlist


class SearchPlaylistsResult(ResponseObject):
    items: list[Playlist]


class SearchResult(TypedDict):
    playlists: SearchPlaylistsResult
