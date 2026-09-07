def input_temperature(temp_str: str) -> int:
    try:
        n = int(temp_str)
    except ValueError:
        raise ValueError("Caught input_temperature error: "
                         "invalid literal for int() with base 10: "
                         f"\'{temp_str}\'")
    return n


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    temp_str_values = ("25", "abc")

    for temp in temp_str_values:
        print(f"Input data is \'{temp}\'")
        try:
            n = input_temperature(temp)
            print(f"Temperature is now {n}°C")
        except ValueError as ve:
            print(ve)
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
