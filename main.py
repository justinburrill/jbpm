"""
- be able to download and automatically install cli programs written by me
- be able to remove installed programs
- list installed programs
    - store config file
"""
import os.path
from pathlib import Path
from config import *


def check_tool_version(tool_name, config):
    installed = get_installed_software(config)
    # TODO: fix


def print_help():
    print(
        """
        Usage:
        jbpm help               - Show this message
        jbpm list               - Lists available software
        jbpm install [name]     - Install software by name
        jbpm uninstall [name]   - Uninstall software by name
        """
    )





def get_relative_path(path):
    cwd = Path.cwd()
    return (cwd / path).resolve()


def err_insufficient_args():
    print("need more args")


def get_config_fp() -> str:
    return os.path.expanduser("~") + "/.jbpmrc"


def get_config():
    config_fp = get_config_fp()
    if not os.path.exists(config_fp):
        print("No config found, creating default")
        create_default_config(config_fp)
    return get_config_dict(config_fp)


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print_help()

    match args[0].lstrip("-"):
        case "h" | "help":
            print_help()
        case "i" | "install":
            if len(args) < 2:
                err_insufficient_args()
                return
            tool_name = args[1]
            install_software(tool_name, get_config())
        case "u" | "uninstall":
            if len(args) < 2:
                err_insufficient_args()
                return
            tool_name = args[1]
            uninstall_software(tool_name)
        case "l" | "list":
            print_installed_tools(get_config())
        case "reset":
            uninstall_all_software(get_config())
            reset_config(get_config_fp())
        case "print":
            print_config(get_config_fp())
        case _:
            print(f"unknown argument {args[0]}")


if __name__ == "__main__":
    main()
