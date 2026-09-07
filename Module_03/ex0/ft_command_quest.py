from sys import argv


def ft_command_quest() -> None:
    def program_name(path: str) -> str:
        flag = 1 if "/" in path else 0
        if not flag:
            return path
        reverse_path = path[::-1]
        i = 0
        for c in reverse_path:
            i += 1
            if c == "/":
                break
        start = len(path) - i + 1
        return path[start:]

    print("=== Command Quest ===")
    print(f"Program name: {program_name(argv[0])}")
    l_argv = len(argv)
    if len(argv) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {l_argv - 1}")
    i = 1
    while i < l_argv:
        print(f"Argument {i}: {argv[i]}")
        i += 1
    print(f"Total arguments: {l_argv}\n")


if __name__ == "__main__":
    ft_command_quest()
