from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import cast


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)

    def show(self) -> None:
        print(f'ID: {self.station_id}\n'
              f'Name: {self.name}\n'
              f'Crew: {self.crew_size} people\n'
              f'Power: {self.power_level}%\n'
              f'Oxygen: {self.oxygen_level}%\n'
              f'Last maintenance: {self.last_maintenance}\n'
              f'Status: {"O" if self.is_operational else "Not o"}perational')


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")

    ss = SpaceStation(
                station_id="ISS001",
                name="International Space Station",
                crew_size=6,
                power_level=85.5,
                oxygen_level=92.3,
                last_maintenance=cast(datetime, "2026-08-29T15:00:00"))
    ss.show()

    print("\n========================================")
    try:
        _ = SpaceStation(
                station_id="ISS001",
                name="International Space Station",
                crew_size=26,
                power_level=85.5,
                oxygen_level=92.3,
                last_maintenance=cast(datetime, "2026-08-29T15:00:00"))

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
