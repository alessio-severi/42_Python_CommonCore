from sys import argv


def ft_score_analytics() -> None:
    def program_name(path: str) -> str:
        return path.split("/")[-1] if "/" in path else path

    def int_parse(arg: str) -> int | None:
        if not arg.isdecimal():
            return print(f"Invalid parameter: \'{arg}\'")
        return int(arg)

    args = [arg for str_arg in copy_argv if (arg := int_parse(
                str_arg)) is not None] if len(copy_argv := argv[1:]) else []

    if not args:
        raise ValueError("No scores provided. Usage: python3 "
                         f"{program_name(argv[0])} <score1> <score2> ...")

    print(f"Scores processed: {args}")
    print(f"Total players: {(n := len(args))}")
    print(f"Total score: {(_sum := sum(args))}")
    print(f"Average score: {_sum / n:.1f}")
    print(f"High score: {(_max := max(args))}")
    print(f"Low score: {(_min := min(args))}")
    print(f"Score range: {_max - _min}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    try:
        ft_score_analytics()
    except ValueError as error:
        print(error)
