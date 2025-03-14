from colours import TerminalColours

colour_for_language = {
    "PS": TerminalColours.LIGHT_BLUE,
    "C#": TerminalColours.BLUE,
    "RUST": TerminalColours.RED,
    "C": TerminalColours.WHITE,
    "F#": TerminalColours.MAGENTA,
    "SH": TerminalColours.LIGHT_GREY,
    "JS": TerminalColours.YELLOW,
}


def language_to_colour(lang: str) -> TerminalColours:
    try:
        return colour_for_language[lang.upper()]
    except KeyError:
        return TerminalColours.WHITE


def get_languages_to_display(lang_dict: dict) -> list[str]:
    raise NotImplementedError
