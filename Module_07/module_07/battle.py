from ex0 import FlameFactory, AquaFactory


if __name__ == "__main__":
    print("Testing factory")
    f = FlameFactory()
    for x in [x1 := f.create_base(), f.create_evolved()]:
        print(x.describe())
        print(x.attack())

    print("\nTesting factory")
    a = AquaFactory()
    for y in [y1 := a.create_base(), a.create_evolved()]:
        print(y.describe())
        print(y.attack())

    print("\nTesting battle")
    print(x1.describe())
    print(" vs.")
    print(y1.describe())
    print(" fight!")
    print(x1.attack())
    print(y1.attack())
