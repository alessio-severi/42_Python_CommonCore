import sys as s
from typing import IO


def ft_print_error(arg: str = "", end: str = "\n") -> None:
    s.stderr.write(f"[STDERR] {arg}{end}")


def ft_print(arg: str = "", end: str = "\n") -> None:
    s.stdout.write(f"{arg}{end}")


def ft_prompt_readln(arg: str) -> str:
    ft_print(arg, "")
    s.stdout.flush()
    result = s.stdin.readline()
    if result and result[-1] == "\n":
        return result[:-1]
    ft_print()
    return result


# Command to remove read permission for the file owner:
# chmod u-r nome_file
def print_ancient_fragment_txt() -> list[str]:
    result: list[str] = []
    if len(s.argv) != 2:
        ft_print("Usage: ft_stream_management.py <file>")
        return result

    ft_print("=== Cyber Archives Recovery & Preservation ===")
    ft_print(f"Accessing file \'{s.argv[1]}\'")
    handle_file: IO[str] | None = None
    try:
        # handle_file: TextIOWrapper but from io import TextIOWrapper
        handle_file = open(file=s.argv[1], mode='r',
                           encoding='utf-8', newline=None)
        result = handle_file.read().splitlines(keepends=True)

        ft_print("---\n")
        for line in result:
            ft_print(line, end="")
        ft_print("\n---")
        return result

    except (FileNotFoundError, PermissionError) as error:
        ft_print_error(f"Error opening file \'{s.argv[1]}\': {error}")
        return result
    finally:
        if handle_file is not None:
            handle_file.close()
            ft_print(f"File \'{s.argv[1]}\' closed.")


def create_new_file(base_file: list[str]) -> list[str]:
    ft_print("\nTransform data: ")
    new_file = [x.replace("\n", "") + "#\n" for x in base_file]

    ft_print("---\n")
    for line in new_file:
        ft_print(line, end="")
    ft_print("\n---")
    return new_file


def save_new_file(name_file: str, new_file: list[str]) -> None:
    handle_file: IO[str] | None = None
    try:

        # handle_file: TextIOWrapper but from io import TextIOWrapper
        handle_file = open(file=name_file, mode='w',
                           encoding='utf-8', newline=None)

        for line in new_file:
            handle_file.write(line)
        ft_print(f"Data saved in file \'{name_file}\'\n")

    except (FileNotFoundError, PermissionError) as error:
        ft_print_error(f"Error opening file \'{name_file}\': {error}")
        ft_print("Data not saved.")
    finally:
        if handle_file is not None:
            handle_file.close()


def run() -> None:
    if not (base_file := print_ancient_fragment_txt()):
        return
    new_file = create_new_file(base_file)
    if not (name_file := ft_prompt_readln("Enter new file name (or empty): ")):
        return ft_print("Not saving data.")
    ft_print(f"Saving data to \'{name_file}\'")
    save_new_file(name_file, new_file)


if __name__ == "__main__":
    run()
