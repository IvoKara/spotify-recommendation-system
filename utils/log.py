from print_color import print as cprint


def slog(text: str):
    cprint(text, tag="success", tag_color="green", color="white")


def dlog(text: str):
    cprint(text, tag="debug", tag_color="black", color="white")


def ilog(text: str):
    cprint(text, tag="info", tag_color="blue", color="white")


def wlog(text: str):
    cprint(text, tag="warning", tag_color="yellow", color="white")


def elog(text: str):
    cprint(text, tag="error", tag_color="red", color="white")
