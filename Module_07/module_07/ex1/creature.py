from ex0.creature import Creature
from .capability import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):

    def attack(self) -> str:
        return super().attack() + "Vine Whip!"

    def heal(self, target: list[Creature]) -> str:
        if not (target and len(target) == 1):
            return "healing error"

        target_name = "itself" if target[0] is self else target[0]._name
        return f"{self._name} heals {target_name} for a small amount"


class Bloomelle(Creature, HealCapability):

    def attack(self) -> str:
        return super().attack() + "Petal Dance!"

    def heal(self, target: list[Creature]) -> str:
        if not (target and all(list(map(lambda x: target.count(x) == 1,
                                        target)))):
            return "healing error"

        if len(target) == 1:
            target_name = "itself" if target[0] is self else target[0]._name
        else:
            target_name = "itself and others" if self in target else "others"
        return f"{self._name} heals {target_name} for a large amount"


class Shiftling(Creature, TransformCapability):

    def __init__(self, creature_type: str) -> None:
        Creature.__init__(self, creature_type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._base_form:
            return super().attack().replace("uses", "attacks") + "normally."
        return f"{self._name} performs a boosted strike!"

    def transform(self) -> str:
        self._base_form = False
        return f"{self._name} shifts into a sharper form!"

    def revert(self) -> str:
        self._base_form = True
        return f"{self._name} returns to normal."


class Morphagon(Creature, TransformCapability):

    def __init__(self, creature_type: str) -> None:
        Creature.__init__(self, creature_type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._base_form:
            return super().attack().replace("uses", "attacks") + "normally."
        return f"{self._name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        self._base_form = False
        return f"{self._name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._base_form = True
        return f"{self._name} stabilizes its form."
