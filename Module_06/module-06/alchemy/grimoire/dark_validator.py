
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    return ingredients + (" - VALID" if any(map(
        lambda x: x in ingredients.lower(), allowed)) else " - INVALID")
