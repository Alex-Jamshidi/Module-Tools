from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_systems: List[str]


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: str


def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_systems:
            possible_laptops.append(laptop)
    return possible_laptops


people = [
    Person(name="Imran", age=22, preferred_operating_systems=["Ubuntu"]),
    Person(name="Eliza", age=34, preferred_operating_systems=["Arch Linux"]),
]

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system="Arch Linux"),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="Ubuntu"),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="ubuntu"),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system="macOS"),
]

for person in people:
    possible_laptops = find_possible_laptops(laptops, person)
    print(f"Possible laptops for {person.name}: {possible_laptops}")

# Try changing the type annotation of Person.preferred_operating_system from str to List[str].
# Run mypy on the code.

# exercise_10.py:29: error: Argument "preferred_operating_system" to "Person" has incompatible type "str"; expected "list[str]"  [arg-type]
# exercise_10.py:30: error: Argument "preferred_operating_system" to "Person" has incompatible type "str"; expected "list[str]"  [arg-type]


# It tells us different places that our code is now wrong, because we’re passing values of the wrong type.
# We probably also want to rename our field - lists are plural. Rename the field to preferred_operating_systems.
# Run mypy again.

# exercise_10.py:23: error: "Person" has no attribute "preferred_operating_system"; maybe "preferred_operating_systems"?  [attr-defined]
# exercise_10.py:29: error: Unexpected keyword argument "preferred_operating_system" for "Person"; did you mean "preferred_operating_systems"?  [call-arg]
# exercise_10.py:30: error: Unexpected keyword argument "preferred_operating_system" for "Person"; did you mean "preferred_operating_systems"?  [call-arg]

# Fix all of the places that mypy tells you need changing. Make sure the program works as you’d expect.