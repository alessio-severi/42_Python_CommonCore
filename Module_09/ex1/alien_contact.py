from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import cast


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_contact(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")
        if (self.contact_type == ContactType.PHYSICAL
                and not self.is_verified):
            raise ValueError("Physical contacts must be verified")
        if (self.contact_type == ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError("Telepathic contact requires at "
                             "least 3 witnesses")
        if (self.signal_strength > 7 and not self.message_received):
            raise ValueError("Strong signals (> 7.0) should include "
                             "received messages")
        return self

    def show(self) -> None:
        mr = self.message_received
        print(f'ID: {self.contact_id}\n'
              f'Type: {self.contact_type.value}\n'
              f'Location: {self.location}\n'
              f'Signal: {self.signal_strength}/10\n'
              f'Duration: {self.duration_minutes} minutes\n'
              f'Witnesses: {self.witness_count}'
              f'{chr(10) + "Message: " + mr if mr else ""}')


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")

    ss = AlienContact(
                contact_id="AC_2024_001",
                location="Area 51, Nevada",
                contact_type=cast(ContactType, "radio"),
                signal_strength=8.5,
                duration_minutes=45,
                witness_count=5,
                message_received="'Greetings from Zeta Reticuli'",
                timestamp=cast(datetime, "2026-08-29T18:00:00"))
    ss.show()

    print("\n========================================")
    try:
        # data: dict[str, object] = {...}
        # AlienContact.model_validate(data)
        _ = AlienContact(
                    contact_id="AC_2024_001",
                    location="Area 51, Nevada",
                    contact_type=cast(ContactType, "telepathic"),
                    signal_strength=8.5,
                    duration_minutes=45,
                    witness_count=2,
                    message_received="'Greetings from Zeta Reticuli''",
                    timestamp=cast(datetime, "2026-08-29T18:00:00"))

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]['ctx']['error'])


if __name__ == "__main__":
    main()
