"""
- be able to download and automatically install cli programs written by me
- be able to remove installed programs
- list installed programs
    - store config file
"""
import os.path
import sys
import json


def create_default_config(fp: str):
    f = open(fp, "x")
    f.write(
        """
        {
            "installed": [
            ]
        }
        """
    )
    f.close()


def get_config_file(fp):
    if not os.path.exists(fp):
        create_default_config(fp)
        return get_config_file(fp)
    with open(fp, "r") as file:
        return json.loads("".join(file.readlines()))


def write_config(fp, config):
    with open(fp, "w") as file:
        file.write(config)


def print_help():
    print("help text")


def print_installed(config):
    installed = config["installed"]
    print("Installed software:")
    if len(installed) == 0:
        print("none. install using ??")
    else:
        for x in installed:
            print(x)


def install_software(toolname, toolldict):
    pass


def uninstall_software(toolname, toolldict):
    pass


def main():
    # (name: url)
    all_tools_dict = {"lll": "https://github.com/justinburrill/lll"}

    args = sys.argv[1:]
    fp = os.path.expanduser("~") + "/.jbpmrc"
    if len(args) > 0:
        if args[0] in ["-h", "--help"]:
            print_help()
            return

    config = get_config_file(fp)
    print_installed(config)


if __name__ == "__main__":
    main()
