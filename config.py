import json
from json import JSONDecodeError

from toolmanager import *


# TODO: finish
def user_setup_config(config: dict) -> dict:
    """
    Prompt user to set all config preference options.
    *Will write the updated config to file*
    :param config: Dict representation of the current config
    :return: Updated config
    """
    try:
        config = user_set_dotnet_install_type(config)
        # TODO: other preferences are set here
        # TODO: powershell script install location
        write_config(config)
        return config
    except KeyError as err:
        error_out("Issue with the config. Try resetting it, sorry.", ConfigError(err))


def get_config_filepath() -> str:
    return os.path.expanduser("~") + "/.jbpm"


def create_default_config() -> dict:
    fp = get_config_filepath()
    try:

        # note that "null" should mean no preference set
        # null in the "uninstalled" section because we haven't fetched the data
        # TODO: generate the "uninstalled" section from some sort of file that keeps tool names and their git links?
        # TODO: powershell default install should be in the same dir as $PROFILE for user install
        #       and "C:\Program Files\PowerShell\Scripts" for all user install
        #       view https://stackoverflow.com/a/67576856
        prefs_dict = {
            "default-install-location": get_system_install_dir(),
            "powershell-script-install-location": get_system_install_dir(),
            "dotnet-install-type": None
        }
        cfg = {
            "preferences": prefs_dict,
            "installed": {
            },
            "uninstalled": {
                "lll": None
            }
        }
        with open(fp, "x") as f:
            f.write(json.dumps(cfg))
        return cfg
    except JSONDecodeError as e:
        error_out(f"Error in decoding JSON config", e)


def user_set_dotnet_install_type(config: dict) -> dict:
    """
    Prompt user to set .NET tools installs type
    :param config: Dict representation of config
    :return: Updated config
    """
    current_value = get_dotnet_install_type(config)
    prompt = "Do you want .NET software to be installed with the runtime included?"
    prompt += "\nThis is only recommended if you do not already have the runtime installed on your system."
    if not current_value:  # null or empty
        prompt += f"\nCurrently you have this set to {current_value}"
    # result = "selfcontained" if user_confirmation(prompt, False) else "dependent"
    result = user_confirmation(prompt, default=False)
    config["preferences"]["dotnet-install-type"] = result
    return config


def get_dotnet_install_type(config: dict) -> str | None:
    install_type = ""
    try:
        install_type = config["preferences"]["dotnet-install-type"]
    except KeyError as e:
        raise ConfigError(f"Config missing: {e}")
    return install_type


def reset_config_and_tools(config: dict):
    fp = get_config_filepath()
    os.remove(fp)
    uninstall_all_software(config)
    new_cfg = create_default_config()
    write_config(new_cfg)


def print_config():
    for line in get_config_file_lines():
        print(line)


def get_config_file_lines():
    with open(get_config_filepath(), "r") as file:
        return file.readlines()


def load_config_or_setup_default():
    if not config_exists():
        config = create_default_config()
        user_setup_config(config)
    return load_config_dict()


def load_config_dict():
    with open(get_config_filepath(), "r") as file:
        return json.loads("".join(file.readlines()))


def write_config(config):
    with open(get_config_filepath(), "w") as file:
        file.write(config)


def check_for_update(config):
    installed = get_installed_software(config)
    #    TODO:
    raise NotImplementedError


def config_exists() -> bool:
    return os.path.exists(get_config_filepath())


def user_prompt(prompt: str, *, default: str = None, check_path_exists: bool = False,
                check_path_permissions: bool = False) -> str | None:
    text = input(prompt)
    if len(text.strip()) == 0:
        return default
    if check_path_exists and not os.path.exists(text):
        raise f"Nothing exists at path {text}."
    if check_path_permissions and not os.access(os.path.dirname(text), os.X_OK):
        raise f"Inadequate permissions for path {text}."

    return text


def user_confirmation(prompt: str, *, default: bool) -> bool:
    txt = f"{prompt} [{'Y' if default else 'y'}/{'N' if not default else 'n'}]\n"
    while True:
        i = input(txt).lower()
        if i == "":
            return default
        if i in ['y', 'yes']:
            return True
        elif i in ['n', 'no']:
            return False
        else:
            print_warning("Huh?")


# TODO: use?
class Preference:
    def __init__(self, name, default):
        self.name = name
        self.default = default
