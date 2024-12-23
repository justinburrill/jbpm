from file import *
from api import *


def install_software(tool_name, config, install_path):
    uninstalled = get_uninstalled_software(config)
    installed = get_installed_software(config)
    if tool_name in installed.keys():
        print(f"Error: Already installed {tool_name}.")
        return
    if tool_name not in uninstalled:
        print(f"Error: Unknown tool {tool_name}")
    try:
        path = save_latest_release_exe(tool_name, install_path)
        path = rename_executable(path)
        make_file_executable(path)
        move_to_bin_dir(path)
    except KeyError:
        print(f"Error: No software named {tool_name}.")
    except PermissionError:
        print(f"Error: Admin permissions required.")
    # except FileExistsError:
    #     print(f"Error: Overwriting existing file.")


def uninstall_all_software(config: dict) -> None:
    installed = get_installed_software(config)
    for tool in installed:
        uninstall_software(tool, config)


def uninstall_software(tool_name: str, config: dict) -> None:
    uninstalled = get_uninstalled_software(config)
    if tool_name not in uninstalled.keys():
        raise FileNotFoundError

    # TODO:


def get_installed_software(config: dict) -> dict:
    return config["installed"]


def get_uninstalled_software(config: dict) -> dict:
    return config["uninstalled"]


def print_tools(config: dict, installed: bool) -> None:
    tools = get_installed_software(config) if installed else get_uninstalled_software(config)
    if installed:
        print("Installed software:")
    else:
        print("Uninstalled software:")
    if len(tools) == 0:
        print("none. try 'jbpm help'")
    else:
        for x in tools:
            print(x)
