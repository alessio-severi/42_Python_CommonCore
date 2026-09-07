from collections.abc import Callable


def spell_combiner(spell1: Callable[[str, int], str],
                   spell2: Callable[[str, int], str]
                   ) -> Callable[[str, int], tuple[str, str]]:
    return lambda x, y: (spell1(x, y), spell2(x, y))


def power_amplifier(base_spell: Callable[[str, int], str],
                    multiplier: int) -> Callable[[str, int], str]:
    return lambda x, y: f"{base_spell(x, y)}, Amplified: {y * multiplier}"


def conditional_caster(condition: Callable[[str, int], bool],
                       spell: Callable[[str, int], str]
                       ) -> Callable[[str, int], str]:
    return lambda x, y: spell(x, y) if condition(x, y) else "Spell fizzled"


def spell_sequence(spells: list[Callable[[str, int], str]]
                   ) -> Callable[[str, int], list[str]]:
    return lambda x, y: [spell(x, y) for spell in spells]


def main() -> None:

    def spell1(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def spell2(target: str, power: int) -> str:
        return f"Heals {target}"

    def base_spell(target: str, power: int) -> str:
        return f"{target}: {power}"

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} with {power} power"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def lightning(target: str, power: int) -> str:
        return f"Lightning strikes {target} with {power} power"

    test_values = [10, 15, 14]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    print("\nTesting spell combiner...")
    print(", ".join(spell_combiner(spell1, spell2)(test_targets[0], 1)))

    print("\nTesting power amplifier...")
    print(power_amplifier(base_spell, 3)("Original", test_values[0]))

    print("\nTesting conditional caster...")
    print(conditional_caster(lambda _, x: x >= 10, spell1)(test_targets[1],
                                                           test_values[1]))

    print("\nTesting spell sequence...")
    print(", ".join(spell_sequence([fireball, heal, lightning])(
        test_targets[2], test_values[2])))


if __name__ == "__main__":
    main()
