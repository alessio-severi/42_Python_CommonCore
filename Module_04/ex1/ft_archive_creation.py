from sys import argv
from typing import IO


# Command to remove read permission for the file owner:
# chmod u-r nome_file
def print_ancient_fragment_txt() -> list[str]:
    result: list[str] = []
    if len(argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return result

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file \'{argv[1]}\'")
    handle_file: IO[str] | None = None
    try:
        # handle_file: TextIOWrapper but from io import TextIOWrapper
        handle_file = open(file=argv[1], mode='r',
                           encoding='utf-8', newline=None)
        result = handle_file.read().splitlines(keepends=True)

        print("---\n")
        for line in result:
            print(line, end="")
        print("\n---")
        return result

    except (FileNotFoundError, PermissionError) as error:
        print(f"Error opening file \'{argv[1]}\': {error}")
        return result
    finally:
        if handle_file is not None:
            handle_file.close()
            print(f"File \'{argv[1]}\' closed.")


def create_new_file(base_file: list[str]) -> list[str]:
    print("\nTransform data: ")
    new_file = [x.replace("\n", "") + "#\n" for x in base_file]

    print("---\n")
    for line in new_file:
        print(line, end="")
    print("\n---")
    return new_file


def save_new_file(name_file: str, new_file: list[str]) -> None:
    handle_file: IO[str] | None = None
    try:
        # handle_file: TextIOWrapper but from io import TextIOWrapper
        handle_file = open(file=name_file, mode='w',
                           encoding='utf-8', newline=None)

        for line in new_file:
            handle_file.write(line)
        print(f"Data saved in file \'{name_file}\'\n")

    except (FileNotFoundError, PermissionError) as error:
        print(f"Error opening file \'{name_file}\': {error}")
        print("Data not saved.")
    finally:
        if handle_file is not None:
            handle_file.close()


def run() -> None:
    if not (base_file := print_ancient_fragment_txt()):
        return
    new_file = create_new_file(base_file)
    if not (name_file := input("Enter new file name (or empty): ")):
        return print("Not saving data.")
    print(f"Saving data to \'{name_file}\'")
    save_new_file(name_file, new_file)


if __name__ == "__main__":
    run()
