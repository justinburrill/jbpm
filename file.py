import os
import platform
import winreg as reg
import traceback

from errors import *


def get_reg_key():
    key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE,
                      r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment",
                      0,
                      reg.KEY_QUERY_VALUE | reg.KEY_SET_VALUE
                      )
    return key


# ChatGPT function 💀💀💀💀
def add_dir_to_path():
    if platform.system().lower() != "windows":
        return

    new_path = get_system_install_dir()
    try:
        # Open the registry key where system PATH is stored
        try:
            key = get_reg_key()
        except PermissionError as err:
            error("Can't open winreg key due to insufficient permissions.", err)
            return
        # Get the current PATH value
        current_path = reg.QueryValueEx(key, "Path")[0]
        print(current_path)

        # Check if the new path is already in PATH
        if new_path not in current_path:
            # Append the new path and set the updated value
            updated_path = current_path + ";" + new_path
            reg.SetValueEx(key, "Path", 0, reg.REG_EXPAND_SZ, updated_path)
            print("Path successfully updated.")
        else:
            print("Path already exists in the system PATH.")

        reg.CloseKey(key)
    except PermissionError:
        print("Error: Admin powers required.\n", traceback.format_exc())


def rename_executable(path: str) -> str:
    path_without_filename, file_name = os.path.split(path)
    if file_name == "":
        raise ValueError("Provided path is a dir, not a file")

    parts = file_name.replace(".", " .").replace("-", " ").split()
    print(file_name, parts)
    file_name = str(parts[0] + (parts[-1] if len(parts) > 2 else ""))
    new_path = os.path.join(path_without_filename, file_name)
    os.rename(path, new_path)
    return new_path


def make_file_executable(path: str):
    """
    Uses chmod on provided file to make it executable
    :param path: Path to the binary file
    """
    # get current permissions of the file
    current_mode = os.stat(path).st_mode
    # 0o444 represents read permissions for owner, group, others
    # should have current file permissions (read) as well as executable permissions
    new_mode = current_mode | (current_mode & 0o444) >> 2
    # apply executable permissions
    os.chmod(path, new_mode)


def get_system_install_dir() -> str:
    match platform.system():
        case "Windows":
            return r"C:\Program Files\jbpm"
        case _:
            return "/user/local/bin"


def move_to_bin_dir(exe_name: str, user_install=False):
    # assuming exe is in the cwd
    folder = get_system_install_dir()
    if not os.path.isdir(folder):
        os.mkdir(folder)
        move_to_bin_dir(exe_name)
    cwd = os.getcwd()
    current_exe_path = os.path.join(cwd, exe_name)
    next_exe_path = os.path.join(folder, exe_name)
    # if os.path.exists(next_exe_path):
    #     raise FileExistsError

    print(exe_name, current_exe_path, next_exe_path)
    os.replace(current_exe_path, next_exe_path)

# def count_occurrences_in_string(char, string) -> int:
#     count = 0
#     chars = list(string)
#     while char in chars:
#         chars.remove(char)
#         count += 1
#     return count
