import functools as f
import operator as op
from collections.abc import Callable
from typing import Any, cast


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    match operation:
        case "add":
            return f.reduce(lambda x, y: op.add(x, y), spells)
        case "multiply":
            return f.reduce(lambda x, y: op.mul(x, y), spells)
        case "max":
            return f.reduce(lambda x, y: max(x, y), spells)
        case "min":
            return f.reduce(lambda x, y: min(x, y), spells)
        case _:
            raise ValueError(f"Invalid operation: \'{operation}\'")


def partial_enchanter(base_enchantment: Callable[..., str]
                      ) -> dict[str, Callable[..., str]]:
    return {base_enchantment.__name__: f.partial(base_enchantment, power=100)}


@f.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        return -1
    if n <= 1:
        return n
    return (memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2))


def spell_dispatcher() -> Callable[[Any], str]:

    @f.singledispatch
    def base_spell(spell: Any) -> str:
        return "Unknown spell type"

    @base_spell.register
    def damage_spell(power: int) -> str:
        return f"{power} damage!"

    @base_spell.register
    def enchantment(enchantment: str) -> str:
        return f"{enchantment}"

    @base_spell.register(list)
    def multi_cast(spells: list[Callable[[Any], str]]) -> str:
        return f"{len(spells)} spells"

    return base_spell


def main() -> None:
    print("Testing spell reducer...")

    name_op = ["Sum", "Product", "Max", "Min", "Division"]
    op_list = ["add", "multiply", "max", "min", "divide"]
    value_list = [[10, 5, 25, 60], [10, 5, 25, 32, 6], [8, 32, 18, 40, 28],
                  [12, 33, 18, 9, 20], [1, 77, 34, 31]]

    for name, op_l, values in zip(name_op, op_list, value_list):
        try:
            print(f'{name}: {spell_reducer(values, op_l)}')

        except ValueError as error:
            print(error)

    print("\nTesting partial enchanter...")

    def spell(power: int, element: str, target: str) -> str:
        return f"{element} hits {target} with {power} power"

    func = spell
    print(op.concat(f'{(name := func.__name__).capitalize()}: ',
                    partial_enchanter(func)[name](element="Fireball",
                                                  target="Dragon")))

    print("\nTesting memoized fibonacci...")

    for n in (0, 1, 10, 15):
        print(f"Fib({n}): {memoized_fibonacci(n)}")

    #   * misses=16 → 16 times it looked for a result that was not yet in the
    #     cache, so it had to calculate it.
    #   * hits=16 → 16 times it found a result already stored in the cache and
    #     returned it without recalculating it.
    #   * maxsize=None → the cache has no size limit.
    #   * currsize=16 → there are currently 16 different results stored in the
    #     cache.
    #   print(memoized_fibonacci.cache_info())
    #
    #   for clear cache use memoized_fibonacci.cache_clear()

    print("\nTesting spell dispatcher...")

    def fireball(power: int) -> str:
        return f"Fireball hits Wizard with {power} power"

    def heal(target: str) -> str:
        return f"Heal restores {target} for 60 HP"

    def lightning(args: list[str]) -> str:
        if len(args) == 2:
            return f"Lightning strikes {args[0]} with {args[1]} power"
        return ""

    fun: "f._SingleDispatchCallable[str]"
    fun = cast("f._SingleDispatchCallable[str]", spell_dispatcher())
    print(f'{fun.dispatch(int).__name__.capitalize().replace("_", " ")}: '
          f'{fun(42)}')
    print(f'{fun.dispatch(str).__name__.capitalize().replace("_", " ")}: '
          f'{fun("fireball")}')
    print(f'{fun.dispatch(list).__name__.capitalize().replace("_", " ")}: '
          f'{fun([fireball, heal, lightning])}')
    print(fun(None))


if __name__ == "__main__":
    main()
