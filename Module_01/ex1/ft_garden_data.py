class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.__name = name
        self.__height = height
        self.__age = age

    def show(self) -> None:
        print(f"{self.__name}: {self.__height:.0f}cm, {self.__age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    for p in [Plant("Rose", 25, 30), Plant("Sunflower", 80, 45),
              Plant("Cactus", 15, 120)]:
        p.show()
