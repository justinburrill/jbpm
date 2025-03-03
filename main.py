"""
- be able to download and automatically install cli programs written by me
- be able to remove installed programs
- list installed programs
    - store config file
"""
import os.path
import sys
import api
from pathlib import Path

import file
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
        jbpm path               - (Windows only) Adds the tool install directory to the windows path
        jbpm install [name]     - Install software by name
        jbpm uninstall [name]   - Uninstall software by name
        jbpm reset              - Uninstall all software
        jbpm clean              - Remove all evidence of jbpm
        """
    )


def get_relative_path(path):
    cwd = Path.cwd()
    return (cwd / path).resolve()


def err_insufficient_args():
    print("Error: Insufficient arguments.")


def get_config_fp() -> str:
    return os.path.expanduser("~") + "/.jbpmrc"


def get_config():
    config_fp = get_config_fp()
    if not os.path.exists(config_fp):
        create_default_config(config_fp)
    return get_config_dict(config_fp)


def user_confirmation(prompt: str, default: bool) -> bool:
    txt = f"{prompt} [{'Y' if default else 'y'}/{'N' if not default else 'n'}]\n"
    while True:
        i = input(txt).lower()
        if i == "":
            return default
        if i in ['y', 'yes']:
            return True
        elif i in ['n', 'no']:
            return False
        else:
            print("Huh?")


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print_help()
        return

    match args[0].lstrip("-"):
        case "h" | "help":
            print_help()
        case "i" | "install":
            if len(args) < 2:
                err_insufficient_args()
                return
            tool_name = args[1]
            install_software(tool_name, get_config(), os.getcwd())
        case "u" | "uninstall":
            if len(args) < 2:
                err_insufficient_args()
                return
            tool_name = args[1]
            try:
                uninstall_software(tool_name, get_config())
            except FileNotFoundError:
                print("Tool {tool_name} not found.")
        case "l" | "list":
            print_tools(get_config(), True)
            print_tools(get_config(), False)
        case "path":
            file.add_dir_to_path()
        case "reset":
            if not user_confirmation("Reset config and uninstall all software?", False):
                return
            reset_config_and_tools(get_config_fp(), get_config())
        case "print":
            print_config(get_config_fp())
        case "clean":
            if not user_confirmation("Clear all config files and software?", False):
                return
            uninstall_all_software(get_config())
            os.remove(get_config_fp())
            dir_path = file.get_system_install_dir()
            if os.path.exists(dir_path):
                os.rmdir(dir_path)

        case _:
            print(f"unknown argument {args[0]}")


if __name__ == "__main__":
    res = api.get_language_breakdown("lll")
    print(res)
    # main()
