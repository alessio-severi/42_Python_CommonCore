class GardenError(Exception):
    def __init__(self, message: str = "Garden is empty") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Missing name") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Outlier detected") -> None:
        super().__init__(message)


# simple demo class Plant
class Plant():
    def __init__(self, name: str, health_requirement: int,
                 water_requirement: float) -> None:
        self._name = name
        self._health_requirement = health_requirement
        self._water_requirement = water_requirement

    def get_name(self) -> str:
        return self._name

    def get_health_requirement(self) -> int:
        return self._health_requirement

    def get_water_requirement(self) -> float:
        return self._water_requirement


# simple demo class Garden
class Garden:
    def __init__(self, name: str):
        self._name = name
        self._plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> str:
        self._plants += [plant]
        return f"Added {plant.get_name()} to {self._name} Garden."

    def get_plants(self) -> list[Plant]:
        return self._plants


def plant_error(plants: Garden, health_level: int) -> None:
    name = plants.get_plants()[0].get_name()
    if plants.get_plants()[0].get_health_requirement() >= health_level:
        raise PlantError(f"The {name} plant is wilting!")


def water_error(plants: Garden, water_level: float) -> None:
    water_requirement = plants.get_plants()[2].get_water_requirement()
    if water_requirement != water_level or not water_level:
        raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting GardenError...")
    plants = Garden("Alex")
    try:
        if not plants.get_plants():
            raise GardenError()
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    print("\nTesting WaterError...")
    plants.add_plant(Plant("tomato", 6, 25))
    water_level = 30.5
    try:
        if plants.get_plants()[0].get_water_requirement() != water_level:
            raise WaterError()
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print("\nTesting PlantError...")
    plants.add_plant(Plant("", 6, 30))
    try:
        if not plants.get_plants()[1].get_name():
            raise PlantError()
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print("\nTesting PlantError...")
    health_level = 3
    try:
        plant_error(plants, health_level)
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print("\nTesting WaterError...")
    plants.add_plant(Plant("captus ", 7, 0))
    water_level = 0
    try:
        water_error(plants, water_level)
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print("\nTesting catching all garden errors...")
    try:
        plant_error(plants, health_level)
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    try:
        water_error(plants, water_level)
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    print("\nAll custom error types work correctly!")
