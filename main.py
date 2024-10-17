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
            "installed": {
            }
        }
        """
    )
    f.close()


def get_config_file():
    fp = os.path.expanduser("~") + "/.jbpmrc"
    if not os.path.exists(fp):
        create_default_config(fp)
    with open(fp, "r") as file:
        return json.loads("".join(file.readlines()))


def print_help():
    print("help text")


def main():
    args = sys.argv[1:]
    if len(args) > 0:
        if args[0] in ["-h", "--help"]:
            print_help()
            return
    config = get_config_file()
    print(config)


if __name__ == "__main__":
    main()
