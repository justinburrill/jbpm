from file import *
from api import *
from errors import *

def install_software(tool_name, config, install_path):
    uninstalled = get_uninstalled_software(config)
    installed = get_installed_software(config)
    if tool_name in installed.keys():
        error(f"Already installed {tool_name}.")
        return
    if tool_name not in uninstalled:
        error(f"Unknown tool {tool_name}.")
        return
    # below is for default executable install
    try:
        path = save_latest_release_exe(tool_name, install_path)
        path = rename_executable(path)
        make_file_executable(path)
        move_to_bin_dir(path)
    except KeyError as err:
        error(f"No software named {tool_name}.", err)
    except PermissionError as err:
        error("Admin permissions required.", err)
    # except FileExistsError:
    #     print(f"Error: Overwriting existing file.")


def uninstall_all_software(config: dict) -> None:
    installed = get_installed_software(config)
    for tool in installed:
        uninstall_software(tool, config)


def uninstall_software(tool_name: str, config: dict) -> None:
    uninstalled = get_uninstalled_software(config)
    if tool_name not in uninstalled.keys():
        error(f"Couldn't find tool {tool_name} to uninstall")

    # TODO: actually uninstall it


def get_installed_software(config: dict) -> dict:
    return config["installed"]


def get_uninstalled_software(config: dict) -> dict:
    return config["uninstalled"]

def install_powershell_script() -> None:
    raise NotImplementedError

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
