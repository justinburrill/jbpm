import json
import os
from toolmanager import *


def reset_config_and_tools(fp: str, config: dict) -> None:
    os.remove(fp)
    uninstall_all_software(config)
    create_default_config(fp)


def create_default_config(fp: str):
    f = open(fp, "x")
    f.write(
        """
{
    "installed": {
    },
    "uninstalled": {
        "lll": null
    }
}
        """
    )
    f.close()


def print_config(fp):
    for line in get_config_file_lines(fp):
        print(line)


def get_config_file_lines(fp):
    with open(fp, "r") as file:
        # return json.loads("".join(file.readlines())) // wtf?
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
