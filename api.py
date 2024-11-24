import requests
import sys
import os
import platform


def get_os_executable_extension():
    osname = platform.system()
    windows = osname == "Windows"
    if windows:
        return "-windows.exe"
    else:
        return "-linux"


def save_latest_release_exe(repo_name: str, install_path: str) -> str:
    s = f"https://github.com/justinburrill/{repo_name}/releases/latest/download/{get_os_executable_extension()}"
    result = requests.get(s, allow_redirects=True)
    path = os.path.join(install_path, repo_name)
    with open(path, 'wb') as f:
        f.write(result.content)
        return path
