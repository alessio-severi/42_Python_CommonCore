def ft_plant_age() -> None:
    print("Plant is ready to harvest!" if int(input(
        "Enter plant age in days: ")) > 60 else
        "Plant needs more time to grow.")
