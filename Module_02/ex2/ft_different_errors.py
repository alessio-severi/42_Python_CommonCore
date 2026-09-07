def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            stringa = "abc"
            try:
                int(stringa)
            except ValueError:
                raise ValueError("Caught ValueError: invalid literal for int()"
                                 f" with base 10:\'{stringa}\'")
        case 1:
            arg1 = 1
            arg2 = 0
            try:
                arg1 / arg2
            except ZeroDivisionError:
                raise ZeroDivisionError("Caught ZeroDivisionError: "
                                        "division by zero")
        case 2:
            file1 = "/non/existent/file"
            try:
                with open(file1, mode="r", encoding="utf-8"):
                    pass
            except FileNotFoundError:
                raise FileNotFoundError("Caught FileNotFoundError: [Errno 2] "
                                        "No such file or directory: "
                                        f"\'{file1}\'")
        case 3:
            arg1 = 1
            stringa = "abc"
            try:
                arg1 + stringa
            except TypeError:
                raise TypeError("Caught TypeError: can only concatenate str "
                                "(not \"int\") to str")

    print("Operation completed successfully")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for i in [0, 1, 2, 3, 4]:
        print(f"Testing operation {i}...")

        # ValueError: converting bad input to int
        # ZeroDivisionError: divide by zero
        # FileNotFoundError: opening a file that doesn't exist
        # TypeError: mixing types that cannot be mixed
        # (adding a string and a number in this case)
        try:
            garden_operations(i)
        except (ValueError, ZeroDivisionError, FileNotFoundError,
                TypeError) as error:
            print(error)

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
