def ft_count_harvest_recursive() -> None:
    def println(tot: int, day: int = 1) -> int:
        return (tot - day) and println(print(f"Day {day}") or tot, day + 1)

    print(println(int(input("Days until harvest: ")) + 1) or "Harvest time!")
