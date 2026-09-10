from abc import ABC, abstractmethod


class Creature(ABC):

    def __init__(self, creature_type: str) -> None:
        self._name = self.__class__.__name__
        self._type = creature_type

    @abstractmethod
    def attack(self) -> str:
        return f"{self._name} uses "

    def describe(self) -> str:
        return (f"{self._name} is a {self._type} type "
                f"{self.__class__.__bases__[0].__name__}")


class Flameling(Creature):

    def attack(self) -> str:
        return super().attack() + "Ember!"


class Pyrodon(Creature):

    def attack(self) -> str:
        return super().attack() + "Flamethrower!"


class Aquabub(Creature):

    def attack(self) -> str:
        return super().attack() + "Water Gun!"


class Torragon(Creature):

    def attack(self) -> str:
        return super().attack() + "Hydro Pump!"
