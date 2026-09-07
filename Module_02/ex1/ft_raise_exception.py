def input_temperature(temp_str: str) -> int:
    try:
        n = int(temp_str)
    except ValueError:
        raise ValueError("Caught input_temperature error: "
                         "invalid literal for int() with base 10: "
                         f"\'{temp_str}\'")
    if n < 0:
        raise ValueError("Caught input_temperature error: "
                         f"{n}°C is too cold for plants (min 0°C)")
    elif n > 40:
        raise ValueError("Caught input_temperature error: "
                         f"{n}°C is too hot for plants (max 40°C)")
    else:
        return n


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")

    temp_str_values = ("25", "abc", "100", "-50")

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
