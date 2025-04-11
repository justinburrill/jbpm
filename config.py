import json
import os
from toolmanager import *


def get_config_filepath() -> str:
    return os.path.expanduser("~") + "/.jbpm"

def create_default_config(fp: str) -> None:
    f = open(fp, "x")
    f.write(
        """
{
    "preferences": {
        "dotnet-install-type": null
    }
    "installed": {
    },
    "uninstalled": {
        "lll": null
    }
}
        """
    )
    f.close()


def user_set_dotnet_install_type(config):
    current = get_dotnet_install_type(config)
    print("Do you want .NET software to be installed with the runtime included?")
    print("This is only recommended if you do not already have the runtime installed on your system.")

def get_dotnet_install_type(config):
    install_type = ""
    try:
        install_type = config["preferences"]["dotnet-install-type"]
    except KeyError as err:
        # config screwed up?
        pass
    return install_type

def reset_config_and_tools(fp: str, config: dict) -> None:
    os.remove(fp)
    uninstall_all_software(config)
    create_default_config(fp)


def print_config(fp):
    for line in get_config_file_lines(fp):
        print(line)


def get_config_file_lines(fp):
    with open(fp, "r") as file:
        return file.readlines()


def get_config_dict(fp):
    with open(fp, "r") as file:
        return json.loads("".join(file.readlines()))


def write_config(fp, config):
    with open(fp, "w") as file:
        file.write(config)


def check_for_update(config):
    installed = get_installed_software(config)
    #    TODO:
    raise NotImplementedError
