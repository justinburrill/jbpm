import json


def create_default_config(fp: str):
    f = open(fp, "x")
    f.write(
        """
{
    "installed": [
    ],
    "uninstalled": [
        "lll": null,
    ]
}
        """
    )  # "installed" entry would look like: "program_name": v1.0,
    f.close()


def get_config_file_lines(fp):
    with open(fp, "r") as file:
        return json.loads("".join(file.readlines()))


def write_config(fp, config):
    with open(fp, "w") as file:
        file.write(config)


def get_installed_tools(config):
    return config["installed"]


def check_for_update(config):
    installed = get_installed_tools(config)
