def rename_executable(path):
    path_without_filename, file_name = remove_filename_from_path(path)
    file_name = str(file_name.split("-")[-1])
    os.rename(path, path_without_filename + find_slash_type(path) + file_name)


def make_file_executable(path):
    current_mode = os.stat(path).st_mode
    new_mode = current_mode | (current_mode & 0o444) >> 2
    os.chmod(path, new_mode)


def move_to_bin_dir(path):
    # TODO: do this
    pass


def count_occurrences_in_string(char, string) -> int:
    count = 0
    chars = list(string)
    while char in chars:
        chars.remove(char)
        count += 1
    return count


# THIS SUCKS USE OS.PATH
def find_slash_type(string) -> str:
    a = '/'
    b = '\\'
    if count_occurrences_in_string(a, string) > count_occurrences_in_string(b, string):
        return a
    else:
        return b


def remove_filename_from_path(path: str) -> (str, str):
    split = map(lambda x: str(x), path.split(find_slash_type(path)))
    filename = split[-1]
    rest = split[:-1]
    return rest, filename
