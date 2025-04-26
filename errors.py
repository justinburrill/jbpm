from colours import *


class JBPMError(BaseException):
    pass


class Api404Error(JBPMError):
    pass


class ConfigError(JBPMError):
    pass


def error_out(message: str = "", err: BaseException = JBPMError()):
    """
    Use for fatal errors. Use `print_error` just to log errors.
    :param message: Text to be added to the error message
    :param err: Pass in the error that already happened. (Is re-thrown)
    :return: Nada
    """
    print_error(message, err)
    raise err


def print_error(message: str, err: BaseException = None):
    err_text = "ERROR" if err is None else f"ERROR ({err.__class__.__name__})"
    print(TerminalColours.coloured(f"{err_text}: {message}\nTraceback:", TerminalColours.RED))
    print(TerminalColours.coloured(err.__traceback__.__str__(), TerminalColours.RED))


def print_warning(message: str):
    print(TerminalColours.coloured(f"WARNING: {message}", TerminalColours.YELLOW))


def err_insufficient_args():
    error_out("Error: Insufficient arguments.")
