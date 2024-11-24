from config import *
from file import *
from api import *


def install_software(tool_name, config):
    uninstalled = get_uninstalled_software(config)
    installed = get_installed_software(config)
    if tool_name in installed.keys():
        print(f"Already installed {tool_name}.")
        return
    try:
        path = save_latest_release_exe(tool_name, install_path)
        make_file_executable(path)
    except KeyError:
        print(f"No software named {tool_name}.")


def uninstall_all_software(config: dict) -> None:
    # TODO:
    pass


def uninstall_software(tool_name: str, config: dict) -> None:
    get_uninstalled_software(config)
    pass


def get_installed_software(config: dict) -> dict:
    return config["installed"]


def get_uninstalled_software(config: dict):
    return config["uninstalled"]


def print_installed_tools(config):
    installed = get_installed_software(config)
    print("Installed software:")
    if len(installed) == 0:
        print("none. try 'jbpm help'")
    else:
        for x in installed:
            print(x)
