from .. import grimoire


def validate_ingredients(ingredients: str) -> str:
    allowed = grimoire.light_spell_allowed_ingredients()
    return ingredients + (" - VALID" if any(map(
        lambda x: x in ingredients.lower(), allowed)) else " - INVALID")
