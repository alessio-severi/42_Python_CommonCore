from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import cast
# from collections.abc import Callable


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M' (Mission)")

        if not any(map(lambda x: x.rank in [
                Rank.COMMANDER, Rank.CAPTAIN], self.crew)):
            raise ValueError("Mission must have at least one Commander "
                             "or Captain")
        if (self.duration_days > 365 and not (len(
            list(filter(lambda x: x.years_experience >= 5, self.crew))) >= len(
                self.crew) / 2)):
            raise ValueError("Long missions (> 365 days) need 50% experienced "
                             "crew (5+ years)")

        if not all(map(lambda x: x.is_active, self.crew)):
            raise ValueError("All crew members must be active")
        return self

    def show(self) -> None:
        print(f'Mission: {self.mission_name}\n'
              f'ID: {self.mission_id}\n'
              f'Destination: {self.destination}\n'
              f'Duration: {self.duration_days} days\n'
              f'Budget: ${self.budget_millions}M\n'
              f'Crew size: {len(self.crew)}\n'
              f'Crew members:')
        for m in self.crew:
            print(f'- {m.name} ({m.rank.value}) - {m.specialization}')


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")

    # CrewMember
    sarah = CrewMember(
        member_id="CM001",
        name="Sarah Connor",
        rank=Rank.COMMANDER,
        age=45,
        specialization="Mission Command",
        years_experience=20,
    )

    john = CrewMember(
        member_id="CM002",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=35,
        specialization="Navigation",
        years_experience=10,
    )

    alice = CrewMember(
        member_id="CM003",
        name="Alice Johnson",
        rank=Rank.OFFICER,
        age=30,
        specialization="Engineering",
        years_experience=7,
    )

    # mission
    sp = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=cast(datetime, "2026-08-30T11:00:00"),
            duration_days=900,
            crew=[sarah, john, alice],
            budget_millions=2500.0)

    sp.show()
    print("\n=========================================")

    try:
        # change CrewMember
        Mario = CrewMember(
            member_id="CM001",
            name="Mark Miles",
            rank=Rank.CADET,
            age=40,
            specialization="Doctor",
            years_experience=10,
        )

        # def f1(**kwargs: object) -> dict[str, object]:
        #     return kwargs
        #
        # Runtime equivalent:
        # f: Callable[..., dict[str, object]] = (lambda **kwargs: kwargs)
        #
        # so you can use f or dict
        _ = SpaceMission.model_validate(dict(
                mission_id="M2024_MARS",
                mission_name="Mars Colony Establishment",
                destination="Mars",
                launch_date="2026-08-29T15:18:00",
                duration_days=900,
                crew=[Mario, john, alice],
                budget_millions=2500.0))

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]['ctx']['error'])


if __name__ == "__main__":
    main()
