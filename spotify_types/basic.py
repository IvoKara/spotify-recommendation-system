from typing import Any, TypedDict


class ResponseObject(TypedDict):
    previous: str | None
    href: str
    next: str | None
    limit: int
    offset: int
    total: int
    items: list[dict[str, Any]]
