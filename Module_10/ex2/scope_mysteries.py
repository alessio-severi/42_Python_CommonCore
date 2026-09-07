from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count

        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    power = initial_power

    def add_power(add: int) -> int:
        nonlocal power

        power += add
        return power

    return add_power


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    type_name = enchantment_type

    def enchantment_description(item_name: str) -> str:
        return f"{type_name} {item_name}"

    return enchantment_description


def memory_vault() -> dict[str, Callable[..., Any]]:
    memory: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        # nonlocal memory
        # memory |= {key: value}
        # or
        memory[key] = value     # memory.update({key: value})

    def recall(key: str) -> Any:
        return memory.get(key, 'Memory not found')

    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    add_power = spell_accumulator(initial := 100)

    for x in (20, 30):
        print(f"Base {initial}, add {x}: {add_power(x)}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")

    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    panel = memory_vault()

    key = 'secret'
    value = 42
    panel['store'](key, value)
    print(f"{panel['store'].__name__.capitalize()} \'{key}\' = {value}")
    print(f"{panel['recall'].__name__.capitalize()} "
          f"\'{key}\' : {panel['recall'](key)}")

    key = 'unknown'
    print(f"{panel['recall'].__name__.capitalize()} "
          f"\'{key}\' : {panel['recall'](key)}")
