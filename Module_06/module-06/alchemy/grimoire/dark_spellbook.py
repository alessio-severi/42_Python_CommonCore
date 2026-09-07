
from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    return (("Spell recorded: " if "VALID"
             in (result := validate_ingredients(ingredients))
             else "Spell rejected: ") + f"{spell_name} ({result})")
