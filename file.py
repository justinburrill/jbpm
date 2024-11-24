import os


def rename_executable(path: str) -> None:
    path_without_filename, file_name = os.path.split(path)
    if file_name == "":
        raise ValueError("Provided path is a dir, not a file")
    file_name = str(file_name.split("-")[-1])
    os.rename(path, os.path.join(path_without_filename, file_name))


def make_file_executable(path: str):
    current_mode = os.stat(path).st_mode
    new_mode = current_mode | (current_mode & 0o444) >> 2
    os.chmod(path, new_mode)


def move_to_bin_dir(path: str):
    # TODO: do this
    pass


def count_occurrences_in_string(char, string) -> int:
    count = 0
    chars = list(string)
    while char in chars:
        chars.remove(char)
        count += 1
    return count
