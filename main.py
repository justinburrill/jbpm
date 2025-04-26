"""
- be able to download and automatically install cli programs written by me
- be able to remove installed programs
- list installed programs
    - store config file

- dotnet projects should have the following options for installation:
    - os specific:
        - self-contained executable
        - framework dependent executable
    - os agnostic (framework dependent):
        - .dll that is run with `dotnet xxx.dll`

- powershell scripts should have these options:
    - download .ps1 and let the user deal with it
    - install as a module so it has autocomplete and everything in the ps shell
        - import-module in profile

- python scripts:
    - download .py itself, up to user to run it how they like
    - shebang it and put it somewhere in the path?
        - ask user for their python interpreter path? get that from system variables?
"""
import os.path
import sys
import api
from pathlib import Path

import file
from config import *
from errors import *


def print_help():
    print(
        """
        Usage:
        jbpm help               - Show this message
        jbpm setup              - Will prompt you to set all preferences
        jbpm fetch              - Check for updates and new software
        jbpm update [all|name]  - Install updates
        jbpm list               - Lists available software
        jbpm addpath            - (Windows only) Adds the tool install directory to the windows path (you gotta figure it out on Linux)
        jbpm install [name]     - Install software by name
        jbpm uninstall [name]   - Uninstall software by name
        jbpm reset              - Reset config and uninstall all software
        jbpm clean              - Remove all evidence of jbpm from your system. Goodbye!
        """
    )


# def get_relative_path(path):
#     cwd = Path.cwd()
#     return (cwd / path).resolve()


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print_help()
        return

    config = load_config_or_setup_default()

    match args[0].lstrip("-"):
        case "h" | "help":
            print_help()
        case "setup":
            user_setup_config(config)
        case "fetch":
            fetch_all_info()
        case "i" | "install":
            if len(args) < 2:
                err_insufficient_args()
                return
            tool_name = args[1]
            install_software(tool_name, config, os.getcwd())
        case "u" | "uninstall":
            if len(args) < 2:
                err_insufficient_args()
                return
            tool_name = args[1]
            try:
                uninstall_software(tool_name, config)
            except FileNotFoundError as err:
                print_error("Tool {tool_name} not found.", err)
        case "l" | "list":
            print_tools(config, True)
            print_tools(config, False)
        case "path":
            file.add_install_dir_to_path()
        case "reset":
            if not user_confirmation("Reset config and uninstall all software?", default=False):
                return
            reset_config_and_tools(config)
        case "print":
            print(f"Config (located at {get_config_filepath()}):")
            print_config()
        case "addpath":
            add_install_dir_to_path()
        case "clean":
            raise NotImplementedError
            if not user_confirmation("Clear all config files and software?", default=False):
                return
            uninstall_all_software(config)
            os.remove(get_config_filepath())
            dir_path = file.get_system_install_dir()
            # TODO: bruhh what is this? im gonna delete "/usr/local/bin"?
            # if os.path.exists(dir_path):
            #    os.rmdir(dir_path)

        case _:
            print_error(f"unknown argument {args[0]}")


if __name__ == "__main__":
    # res = api.get_language_breakdown("lll")
    # print(res)
    try:
        main()
    except BaseException as err:
        # not erroring out here cuz its over anyway
        print_error(f"Critical failure due to: {err}")
