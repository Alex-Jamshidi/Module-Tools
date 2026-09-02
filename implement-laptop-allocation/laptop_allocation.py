# ----- Imports
from dataclasses import dataclass
from enum import Enum

# ----- Classes
class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    # Sorted in order of preference, most preferred is first.
    preferred_operating_systems: list[OperatingSystem]


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

# ----- Functions
def allocate_laptops(people: list[Person], laptops: list[Laptop]) -> dict[Person, Laptop]:
    print("allocating laptops...")
    return

