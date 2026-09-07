class GardenError(Exception):
    def __init__(self, message: str = "Garden is empty") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Missing name") -> None:
        super().__init__(message)


# simple demo class Plant
class Plant():
    def __init__(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: \'{plant_name}\'"
                         "\n.. ending tests and returning to main")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants: list[Plant]) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant.get_name())
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")

    print("\nTesting valid plants...")
    test_watering_system([Plant("Tomato"), Plant("Lettuce"), Plant("Carrots")])

    print("\nTesting invalid plants...")
    test_watering_system([Plant("Tomato"), Plant("lettuce"), Plant("Carrots")])

    print("\nCleanup always happens, even with errors!")
