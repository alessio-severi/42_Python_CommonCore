from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability
from .dedicated_exception import CreatureStrategyMismatchError


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise CreatureStrategyMismatchError(
                             "Battle error, aborting tournament: "
                             f"Invalid Creature '{creature._name}' "
                             "for this normal strategy")
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, Creature)
                and isinstance(creature, TransformCapability))

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise CreatureStrategyMismatchError(
                             "Battle error, aborting tournament: "
                             f"Invalid Creature '{creature._name}' "
                             "for this aggressive strategy")
        assert isinstance(creature, TransformCapability)
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, Creature)
                and isinstance(creature, HealCapability))

    def act(self, creature: Creature, target: list[Creature] = []) -> None:
        if not self.is_valid(creature):
            raise CreatureStrategyMismatchError(
                             "Battle error, aborting tournament: "
                             f"Invalid Creature '{creature._name}' "
                             "for this defensive strategy")
        assert isinstance(creature, HealCapability)
        print(creature.attack())
        print(creature.heal(target))
