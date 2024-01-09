def url_to_uri(url: str) -> str:
    resource, id = url.split("/")[-2:]
    return f"spotify:{resource}:{id}"


def url_to_id(url: str) -> str:
    return url.split("/")[-1]
