def prepare(track: dict) -> dict:
    album_images: list = track["album"]["images"]

    prepared = {
        "track_id": track["id"],
        "track_name": track["name"],
        "artists": [artist["name"] for artist in track["artists"]],
        "image_url": album_images[0]["url"] if album_images else None,
        "release_date": track["album"]["release_date"],
    }

    return prepared


def is_valid(track: dict) -> bool:
    # Instruct Ruff to remain it on multiple lines
    return (
        track is not None  # noqa
        and track["id"] is not None
        and track["name"] is not None
    )
