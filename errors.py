from colours import *


class JBPMError(BaseException):
    pass


class Api404Error(JBPMError):
    pass


class ConfigError(JBPMError):
    pass


def error_out(message: str = "", err: BaseException = JBPMError()) -> None:
    print_error(message, err)
    raise err


def print_error(message: str, err: BaseException = None):
    err_text = "ERROR" if err is None else f"ERROR: {err.__class__.__name__}"
    print(TerminalColours.coloured(f"{err_text}: {message}", TerminalColours.RED))


def print_warning(message: str):
    print(TerminalColours.coloured(f"ERROR: {message}", TerminalColours.YELLOW))


def err_insufficient_args():
    print_error("Error: Insufficient arguments.")
