class Plant:

    class Statistics:
        def __init__(self) -> None:
            self._number_grow = 0
            self._number_age = 0
            self._number_show = 0

        def show(self) -> None:
            print(f"Stats: {self._number_grow} grow, "
                  f"{self._number_age} age, "
                  f"{self._number_show} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self.set_height(height)
        self.set_age(age)
        self._state = self.__class__.Statistics()

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
        self._state._number_grow += 1

    def age(self) -> None:
        self._age += 1
        self._state._number_age += 1

    @staticmethod
    def check_year_old(age: int) -> None:
        print(f"Is {age} days more than a year? -> {age > 365}")

    @classmethod
    def create_anonymous_class(cls, name: None | str = None,
                               height: None | float = None,
                               age: None | int = None) -> "Plant | None":
        return cls("Unknown plant", 0.0, 0) if (
            None in [name, height, age]) else None

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")
        self._state._number_show += 1

    def statistics_show(self) -> None:
        self._state.show()


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int,
                 color: str, bloom_status: bool) -> None:
        super().__init__(name, height, age)
        self._color = color
        self.set_bloom_status(bloom_status)

    def set_bloom_status(self, bloom_status: bool) -> None:
        if (bloom_status):
            self.bloom()
        else:
            self.bloom_off()

    def bloom(self) -> None:
        self._bloom_status = True

    def bloom_off(self) -> None:
        self._bloom_status = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloom_status:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):

    class Statistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._number_produce_shade = 0

        def show(self) -> None:
            super().show()
            print(f"{self._number_produce_shade} shade")

    _state: "Tree.Statistics"

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
        self._state._number_produce_shade += 1

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


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str, bloom_status: bool) -> None:
        super().__init__(name, height, age, color, bloom_status)

    def bloom(self) -> None:
        super().bloom()
        self._seed_number = 42

    def bloom_off(self) -> None:
        super().bloom_off()
        self._seed_number = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seed_number}")


def garden_statistics(plant: Plant) -> None:
    plant.statistics_show()


if __name__ == "__main__":

    print("=== Garden statistics ===")
    height, age = 15.0, 30
    try:
        p = Plant("Rose", height, age)
        print("=== Check year-old")
        p.check_year_old(p.get_age())
        p.set_age(400)
        p.check_year_old(p.get_age())
    except ValueError as vs:
        print(vs)

    print("\n=== Flower")
    height, age = 15.0, 10
    try:
        p = Flower("Rose", height, age, "red", False)
        p.show()
        garden_statistics(p)
        p.grow(8)
        p.bloom()
        p.show()
        garden_statistics(p)
    except ValueError as vs:
        print(vs)

    print("\n=== Tree")
    height, age, trunk_diameter = 200.0, 365, 5.0
    try:
        p = Tree("Oak", height, age, trunk_diameter)
        p.show()
        garden_statistics(p)
        p.produce_shade()
        garden_statistics(p)
    except ValueError as vs:
        print(vs)

    print("\n=== Seed")
    height, age = 80.0, 45
    try:
        p = Seed("Sunflower", height, age, "yellow", False)
        p.show()
        p.set_age(64)
        p.age()
        p.grow(30)
        p.bloom()
        p.show()
        garden_statistics(p)
    except ValueError as vs:
        print(vs)

    print("\n=== Anonymous")
    data = ()
    p1 = Plant.create_anonymous_class(*data)
    if p1 is not None:
        p1.show()
        garden_statistics(p1)
    else:
        print("0 Unknown plant saved")
