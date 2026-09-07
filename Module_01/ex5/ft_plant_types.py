class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: float) -> None:
        if height < 0:
            raise ValueError(f"{self._name}: "
                             "Error, height can't be negative\n"
                             "Height update rejected")
        self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            raise ValueError(f"{self._name}: "
                             "Error, age can't be negative\n"
                             "Age update rejected")
        self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def grow(self, delta_height: float) -> None:
        self._height += delta_height

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str, bloom_status: bool) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloom_status = bloom_status

    def bloom(self) -> None:
        self._bloom_status = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloom_status:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.set_trunk_diameter(trunk_diameter)

    def set_trunk_diameter(self, trunk_diameter: float) -> None:
        if trunk_diameter < 0:
            raise ValueError(f"{self._name}: "
                             "Error, trunk_diameter can't be negative\n"
                             "Trunk diameter update rejected")
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height:.1f}cm long and "
              f"{self._trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.set_harvest_season(harvest_season)
        self._nutritional_value = 0
        self._nutritional_status = 0

    def set_harvest_season(self, harvest_season: str) -> None:
        if harvest_season not in ["January", "February", "March", "April",
                                  "May", "June", "July", "August", "September",
                                  "October", "November", "December"]:
            raise ValueError(f"{self._name}: "
                             "Error, invalid harvest season\n"
                             "Harvest season update rejected")
        self._harvest_season = harvest_season

    def grow(self, delta_height: float) -> None:
        super().grow(delta_height)
        self.nutritional_status_utils()

    def age(self) -> None:
        super().age()
        self.nutritional_status_utils()

    def nutritional_status_utils(self) -> None:
        self._nutritional_status += 1
        if self._nutritional_status == 2:
            self._nutritional_value += 1
            self._nutritional_status = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    height, age = 15.0, 10
    try:
        p = Flower("Rose", height, age, "red", False)
        p.show()
        p.bloom()
        p.show()
    except ValueError as vs:
        print(vs)

    print("\n=== Tree")
    height, age, trunk_diameter = 200.0, 365, 5.0
    try:
        p1 = Tree("Oak", height, age, trunk_diameter)
        p1.show()
        p1.produce_shade()
    except ValueError as vs:
        print(vs)

    print("\n=== Vegetable")
    height, age, harvest_season = 5.0, 10, "April"
    try:
        p2 = Vegetable("Tomato", height, age, harvest_season)
        p2.show()
        for i in range(20):
            p2.age()
            p2.grow(2.1)
        p2.show()
    except ValueError as vs:
        print(vs)
