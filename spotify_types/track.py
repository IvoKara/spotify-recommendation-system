from typing import TypedDict

from .album import Album
from .artist import Artist


class Track(TypedDict):
    id: str
    name: str
    href: str
    popularity: int
    album: Album
    artists: list[Artist]
    available_markets: list[str]
    disc_number: int
    duration_ms: int
    explicit: bool
    preview_url: str | None
    is_local: bool


class TrackAudioFeatures(TypedDict):
    id: str
    acousticness: float
    analysis_url: str
    danceability: float
    duration_ms: int
    energy: float
    instrumentalness: float
    key: int
    liveness: float
    loudness: float
    mode: int
    speechiness: float
    tempo: float
    time_signature: int
    track_href: str
    valence: float
