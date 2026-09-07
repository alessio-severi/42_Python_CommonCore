class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.__name = name
        self.__height = height
        self.__age = age
        print("Created:", end=" ")
        self.show()

    def show(self) -> None:
        print(f"{self.__name}: {self.__height:.1f}cm, {self.__age} days old")

    def grow(self, delta_height: float) -> None:
        self.__height += delta_height

    def age(self) -> None:
        self.__age += 1


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    [_ for _ in [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)]]
