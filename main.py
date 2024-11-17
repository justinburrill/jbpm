"""
- be able to download and automatically install cli programs written by me
- be able to remove installed programs
- list installed programs
    - store config file
"""
import os.path
from pathlib import Path
from api import *
from config import *


def check_tool_version(tool_name, config):
    installed = get_installed_tools(config)


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


def get_os_executable_extension():
    windows = True
    if windows:
        return "-windows.exe"
    else:
        return "-linux"


def get_relative_path(path):
    cwd = Path.cwd()
    return (cwd / path).resolve()


def main():
    # (name: url)
    all_tools_dict = {"lll.exe": "https://github.com/justinburrill/lll"}

    args = sys.argv[1:]
    config_fp = os.path.expanduser("~") + "/.jbpmrc"
    if len(args) == 0:
        print_help()

    if not os.path.exists(config_fp):
        print("No config found, creating default")
        create_default_config(config_fp)

    config = get_config_file_lines(config_fp)

    match args[0]:
        case "-h" | "--help":
            print_help()
            return
        case _:
            print(f"unknown argument {args[0]}")
            return

    # path = save_latest_release_exe("lll.exe", get_relative_path("."))
    # make_file_executable(path)


if __name__ == "__main__":
    main()
