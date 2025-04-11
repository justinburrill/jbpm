from colours import *

class JBPMError(BaseException):
    pass

class Api404Error(JBPMError):
    pass

def error(message: str = "", err_type: BaseException = JBPMError) -> None:
    print(TerminalColours.coloured(f"ERROR: {message}", TerminalColours.RED))
    raise err_type


def err_insufficient_args():
    print("Error: Insufficient arguments.")


