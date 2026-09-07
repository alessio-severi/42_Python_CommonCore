import alchemy.elements
import elements


def healing_potion() -> str:
    return ("Healing potion brewed with "
            f"\'{alchemy.elements.create_earth()}\' and"
            f" \'{alchemy.elements.create_air()}\'")


def strength_potion() -> str:
    return ("Strength potion brewed with "
            f"\'{elements.create_fire()}\' and"
            f" \'{elements.create_water()}\'")
