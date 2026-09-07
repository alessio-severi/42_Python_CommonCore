class Plant:
    _name: str
    _height: float
    _age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self.set_height(height)
        self.set_age(age)
        print(f"Plant created: {self._name}: "
              f"{self._height:.1f}cm, {self._age} days old")

    def set_height(self, height: float) -> None:
        if height < 0:
            raise ValueError(f"{self._name}: "
                             "Error, height can't be negative\n"
                             "Height update rejected")
        try:
            self._height
            print(f"Height updated: {height:.0f}cm")
        except AttributeError:
            pass
        self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            raise ValueError(f"{self._name}: "
                             "Error, age can't be negative\n"
                             "Age update rejected")
        try:
            self._age
            print(f"Age updated: {age} days old")
        except AttributeError:
            pass
        self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"Current state: "
              f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self, delta_height: float) -> None:
        self._height += delta_height

    def age(self) -> None:
        self._age += 1


if __name__ == "__main__":
    print("=== Garden Security System ===")
    p = Plant("Rose", 15.0, 10)
    print()

    for tupla in [(25, 30), (-25, -30)]:
        try:
            p.set_height(tupla[0])
        except ValueError as vs:
            print(vs)
        try:
            p.set_age(tupla[1])
        except ValueError as vs:
            print(vs)
        print()

    p.show()
