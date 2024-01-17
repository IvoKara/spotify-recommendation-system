from typing import TypedDict


class Image(TypedDict):
    url: str
    height: int | None
    width: int | None
