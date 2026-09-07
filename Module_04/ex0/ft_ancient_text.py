from sys import argv
from typing import IO


# Command to remove read permission for the file owner:
# chmod u-r nome_file
def print_ancient_fragment_txt() -> None:
    if len(argv) != 2:
        return print("Usage: ft_ancient_text.py <file>")

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file \'{argv[1]}\'")
    handle_file: IO[str] | None = None
    try:
        # handle_file: TextIOWrapper but from io import TextIOWrapper
        handle_file = open(file=argv[1], mode='r', encoding='utf-8')
        print(f"---\n\n{handle_file.read()}\n\n---")

    except (FileNotFoundError, PermissionError) as error:
        print(f"Error opening file \'{argv[1]}\': {error}")
    finally:
        if handle_file is not None:
            handle_file.close()
            print(f"File \'{argv[1]}\' closed.")


if __name__ == "__main__":
    print_ancient_fragment_txt()
