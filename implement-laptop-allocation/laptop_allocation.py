# ----- Imports
from dataclasses import dataclass
from enum import Enum

from scipy.optimize import linear_sum_assignment


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
    preferred_operating_systems: tuple[OperatingSystem, ...]


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


# ----- Functions
def allocate_laptops(
    people: list[Person], laptops: list[Laptop]
) -> dict[Person, Laptop]:
    cost_matrix = []
    for person in people:
        person_costs = []
        for laptop in laptops:
            if laptop.operating_system in person.preferred_operating_systems:
                sadness = person.preferred_operating_systems.index(
                    laptop.operating_system
                )
            else:
                sadness = 100
            person_costs.append(sadness)
        cost_matrix.append(person_costs)

    row_ind, col_ind = linear_sum_assignment(cost_matrix)

    return {
        people[p_index]: laptops[l_index] for p_index, l_index in zip(row_ind, col_ind)
    }
