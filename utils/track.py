def prepare(track: dict) -> dict:
    album_images = track["album"]["images"]

    prepared = {
        "track_id": track["id"],
        "track_name": track["name"],
        "artists": [artist["name"] for artist in track["artists"]],
        "image_url": album_images[0]["url"] if len(album_images) else None,
        "release_date": track["album"]["release_date"],
    }

    return prepared
