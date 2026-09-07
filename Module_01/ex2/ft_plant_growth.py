class Plant:
    _Plant__name: str
    _Plant__height: float
    _Plant__age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self.__name = name
        self.__height = height
        self.__age = age

    def show(self) -> None:
        print(f"{self.__name}: {self.__height:.1f}cm, {self.__age} days old")

    def grow(self, delta_height: float) -> None:
        self.__height += delta_height

    def age(self) -> None:
        self.__age += 1


if __name__ == "__main__":
    p = Plant(*(init_p := ("Rose", 25, 30)))
    print("=== Garden Plant Growth ===")
    p.show()

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        p.grow(0.8)
        p.age()
        p.show()
        if (i == 7):
            print(f"Growth this week: {p._Plant__height - init_p[1]:.1f}cm")
