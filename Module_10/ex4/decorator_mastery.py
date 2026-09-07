from collections.abc import Callable
from functools import wraps    # partial, update_wrapper
import time
from typing import Any


def spell_timer(func: Callable[..., Any]
                ) -> Callable[..., Any]:

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result

    # @wraps(func)
    # is equivalent to
    # decorator: Callable[[Callable], Any] = wraps(func)
    # wrapper = decorator(wrapper)
    return wrapper


def power_validator(min_power: int
                    ) -> Callable[[Callable[..., str]], Callable[..., str]]:
    def decorator(spell: Callable[..., str]
                  ) -> Callable[..., str]:

        flag = spell.__qualname__.startswith("MageGuild.")

        @wraps(spell)
        def wrapper(instance: "MageGuild | None", target: str, power: int
                    ) -> str:
            if power >= min_power:
                return (spell(instance, target, power) if flag
                        else spell(target, power))
            return "Insufficient power for this spell"

        # return (wrapper if flag else update_wrapper(
        #        partial(wrapper, None), wrapper))   # instance=None
        # or
        @wraps(spell)
        def standalone_wrapper(target: str, power: int) -> str:
            return wrapper(None, target, power)

        return wrapper if flag else standalone_wrapper
    return decorator


def retry_spell(max_attempts: int
                ) -> Callable[[Callable[[str, int], str]],
                              Callable[[str, int], str]]:
    def decorator(spell: Callable[[str, int], str]
                  ) -> Callable[[str, int], str]:

        @wraps(spell)
        def wrapper(target: str, power: int) -> str:
            for i in range(1, max_attempts + 1):
                try:
                    return spell(target, power)
                except Exception:
                    if i < max_attempts:
                        print("Spell failed, retrying... "
                              f"(attempt {i}/{max_attempts})")

            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c == " " for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:

    print("Testing spell timer...")

    @spell_timer
    def fireball(power: int) -> str:
        return f"Fireball hits Wizard with {power} power"

    # @spell_timer
    # is equivalent to
    # fireball = spell_timer(fireball)
    print(f"Result: {fireball(40)}")

    print("\nTesting power validator...")

    @power_validator(40)
    def lightning(target: str, power: int) -> str:
        return f"Lightning strikes {target} with {power} power"

    print(sp := f"{lightning.__name__.capitalize()} spell...")
    print(lightning("Knight", 50))
    print(sp)
    print(lightning("Knight", 30))

    print("\nTesting retry spell...")

    @retry_spell(3)
    def heal(target: str, power: int) -> str:
        if power >= 40:
            return f"Heal restores {target} for {power} HP"
        raise ValueError("Low power level")

    print(sp := f"{heal.__name__.capitalize()} spell... Waaaaaaagh")
    print(heal("Goblin", 50))
    print(sp)
    print(heal("Goblin", 20))

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Wizard"))
    print(MageGuild.validate_mage_name("  "))
    print((m := MageGuild()).cast_spell("Lightning", 15))
    print(m.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
