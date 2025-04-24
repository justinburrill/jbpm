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


def get_git_base_repo_url(repo_name: str) -> str:
    return f"https://github.com/justinburrill/{repo_name}"


def get_git_base_api_url(repo_name: str) -> str:
    return f"https://api.github.com/repos/justinburrill/{repo_name}"


def get_git_repo_dl_url(repo_name: str, file_name: str) -> str:
    return f"{get_git_base_repo_url(repo_name)}/releases/latest/download/{file_name}"


def fetch_language_breakdown(repo_name: str) -> dict:
    url = f"{get_git_base_api_url(repo_name)}/languages"
    result = requests.get(url, allow_redirects=True)
    if result.status_code == 404:
        raise Api404Error(f"Couldn't get language breakdown of {repo_name}, probably due to bad request url")
    return dict(result.json())


def fetch_file_from_latest_release(repo_name: str, *, install_path: str, file_name: str) -> str:
    """
    Downloads a file from repo_name/file_name to install_path.
    :param repo_name: Github repository name for the project (justinburrill/repo_name)
    :param install_path: Local path to place the new file
    :param file_name: Name of the file to download (by default, try to download a repo_name.exe)
    :return: The local path of the file after it is downloaded
    """
    url = get_git_repo_dl_url(repo_name, file_name)
    result = requests.get(url, allow_redirects=True)
    path = os.path.join(install_path, file_name)
    with open(path, 'wb') as f:
        f.write(result.content)
        return file_name
