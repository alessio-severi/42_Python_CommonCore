
# Command to remove read and write permission for the file owner:
# chmod u-rw nome_file
def read_file(name_file: str) -> tuple[bool, str]:
    result_flag: bool
    header: str
    message: str
    try:
        with open(file=name_file, mode='r',
                  encoding='utf-8', newline=None) as handle_file:
            header = "Using 'secure_archive' to read from a regular file:"
            message = handle_file.read()
            result_flag = True

    except (FileNotFoundError, PermissionError) as error:
        if "[Errno 2]" in f"{error}":
            header = ("Using 'secure_archive' to read from"
                      " a nonexistent file:")
        else:
            header = ("Using 'secure_archive' to read from"
                      " an inaccessible file:")
        message = f"{error}"
        result_flag = False

    print(header)
    return (result_flag, message)


def write_file(name_file: str, text: str) -> tuple[bool, str]:
    result_flag: bool
    header: str
    message: str
    try:
        with open(file=name_file, mode='w',
                  encoding='utf-8', newline=None) as handle_file:
            handle_file.write(text)
            header = ("Using 'secure_archive' to write previous "
                      "content to a new file:")
            message = "Content successfully written to file"
            result_flag = True

    except (FileNotFoundError, PermissionError) as error:
        if "[Errno 2]" in f"{error}":
            header = ("Using 'secure_archive' to write to"
                      " a nonexistent file:")
        else:
            header = ("Using 'secure_archive' to write to"
                      " an inaccessible file:")
        message = f"{error}"
        result_flag = False

    print(header)
    return (result_flag, message)


def secure_archive(name_file: str, std: int = 0,
                   text: str = "") -> tuple[bool, str]:
    return write_file(name_file, text) if std else read_file(name_file)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    text = ("[FRAGMENT 001] Digital preservation protocols established 2087\n"
            "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
            "[FRAGMENT 003] Every byte saved is a victory against oblivion\n")
    test: list[tuple[str] | tuple[str, int, str]] = [
            ("/not/existing/file",),
            ("master.password",),
            ("ancient_fragment.txt",),
            ("/not/existing/file", 1, text),
            ("master.password", 1, text),
            ("ancient_fragment_copy.txt", 1, text)]
    for x in test:
        print(secure_archive(*x))
        print()
