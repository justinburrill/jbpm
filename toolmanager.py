from file import *
from api import *
from errors import *
from enum import Enum


class ProjectType(Enum):
    Default, Dotnet, Powershell, Rust, Python = range(5)


def get_project_type(tool_name) -> ProjectType:
    try:
        langs = get_language_breakdown(tool_name)
    except Api404Error as err:
        return ProjectType.Default
    match max(langs, key=langs.get):
        case "Rust":
            return ProjectType.Rust
        case "Python":
            return ProjectType.Python
        case "C#" | "F#":
            return ProjectType.Dotnet
        case "Powershell":
            return ProjectType.Powershell
        case _:
            return ProjectType.Default


def check_tool_version(tool_name, config):
    installed = get_installed_software(config)
    # TODO: finish


def install_software(tool_name, config, install_path):
    uninstalled = get_uninstalled_software(config)
    installed = get_installed_software(config)
    if tool_name in installed.keys():
        error(f"Already installed {tool_name}.")
        return
    if tool_name not in uninstalled:
        error(f"Unknown tool {tool_name}.")
        return
    match get_project_type(tool_name):
        case ProjectType.Dotnet:
            install_software_dotnet(tool_name, config, install_path)
        case ProjectType.Powershell:
            install_powershell_script()
        case _:
            install_software_default(tool_name, config, install_path)


def install_software_default(tool_name, config, install_path):
    try:
        path = save_latest_release_exe(tool_name, install_path)
        path = rename_executable(path)
        make_file_executable(path)
        move_to_bin_dir(path)
    except KeyError as err:
        error(f"No software named {tool_name}.", err)
    except PermissionError as err:
        error("Admin permissions required.", err)


def install_software_dotnet(tool_name, config, install_path):
    pass

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
