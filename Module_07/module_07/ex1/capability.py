from abc import ABC, abstractmethod
from ex0.creature import Creature


class HealCapability(ABC):

    @abstractmethod
    def heal(self, target: list[Creature]) -> str:
        pass


class TransformCapability(ABC):

    def __init__(self) -> None:
        self._base_form = True

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
