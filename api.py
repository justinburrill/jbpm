import requests
import os
import platform
from errors import *


def get_os_executable_extension():
    osname = platform.system()
    windows: bool = osname == "Windows"
    if windows:
        return "-windows.exe"
    else:
        return "-linux"


def get_github_base_repo_url(repo_name: str) -> str:
    return f"https://github.com/justinburrill/{repo_name}"


def get_github_base_api_url(repo_name: str) -> str:
    return f"https://api.github.com/repos/justinburrill/{repo_name}"


def get_language_breakdown(repo_name: str) -> dict:
    query = f"{get_github_base_api_url(repo_name)}/languages"
    #print(f"query at {query}")
    result = requests.get(query, allow_redirects=True)
    if result.status_code == 404:
        raise Api404Error(f"Couldn't get language breakdown of {repo_name}, probably due to bad request url")
    return dict(result.json())


def save_latest_release_exe(repo_name: str, install_path: str) -> str:
    exe_name = f"{repo_name}{get_os_executable_extension()}"
    s = f"{get_github_base_repo_url(repo_name)}/releases/latest/download/{exe_name}"
    # print(s)
    result = requests.get(s, allow_redirects=True)
    path = os.path.join(install_path, exe_name)
    with open(path, 'wb') as f:
        f.write(result.content)
        return exe_name
