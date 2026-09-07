from .. import grimoire


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    return (("Spell recorded: " if "VALID"
             in (result := grimoire.validate_ingredients(ingredients))
             else "Spell rejected: ") + f"{spell_name} ({result})")
