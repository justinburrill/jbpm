from config import *
from file import *
from api import *


def install_software(tool_name, tool_dict):
    url = tool_dict[tool_name]
    path = save_latest_release_exe(tool_name, url)
    make_file_executable(path)


def uninstall_software(tool_name, tool_dict):
    # TODO: do this
    pass


def print_installed_tools(config):
    installed = get_installed_tools(config)
    print("Installed software:")
    if len(installed) == 0:
        print("none. try 'jbpm help'")
    else:
        for x in installed:
            print(x)
