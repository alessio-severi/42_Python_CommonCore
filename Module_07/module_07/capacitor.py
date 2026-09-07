from ex1 import HealingCreatureFactory, TransformCreatureFactory
from typing import Any


if __name__ == "__main__":
    print("Testing Creature with healing capability")

    h = HealingCreatureFactory()
    print(" base:")
    x: Any
    for x in [x1 := h.create_base(), h.create_evolved()]:
        print(x.describe())
        print(x.attack())
        if x is x1:
            print(x1.heal([x1]))
            print(" evolved:")
        else:
            print(x.heal([x1, x]))

    print("\nTesting Creature with transform capability")

    t = TransformCreatureFactory()
    print(" base:")
    y: Any
    for y in [y1 := t.create_base(), t.create_evolved()]:
        print(y.describe())
        print(y.attack())
        print(y.transform())
        print(y.attack())
        print(y.revert())
        if y is y1:
            print(" evolved:")
