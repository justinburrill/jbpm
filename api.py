import requests
import os
import platform


def get_os_executable_extension():
    osname = platform.system()
    windows: bool = osname == "Windows"
    if windows:
        return "-windows.exe"
    else:
        return "-linux"


def save_latest_release_exe(repo_name: str, install_path: str) -> str:
    exe_name = f"{repo_name}{get_os_executable_extension()}"
    s = f"https://github.com/justinburrill/{repo_name}/releases/latest/download/{exe_name}"
    # print(s)
    result = requests.get(s, allow_redirects=True)
    path = os.path.join(install_path, exe_name)
    with open(path, 'wb') as f:
        f.write(result.content)
        return exe_name
