def prepare(track: dict) -> dict:
    prepared = {
        "track_id": track["id"],
        "track_name": track["name"],
        "artists": [artist["name"] for artist in track["artists"]],
        "image_url": track["album"]["images"][0]["url"],
        "release_date": track["album"]["release_date"],
    }

    return prepared
