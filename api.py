import requests
import sys

from main import get_os_executable_extension


def save_latest_release_exe(repo_name, install_path) -> str:
    s = f"https://github.com/justinburrill/{repo_name}/releases/latest/download/{get_os_executable_extension()}"
    result = requests.get(s, allow_redirects=True)
    path = install_path / repo_name
    with open(path, 'wb') as f:
        f.write(result.content)
        return path
