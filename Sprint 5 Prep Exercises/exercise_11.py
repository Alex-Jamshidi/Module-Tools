# Write a program which:

# Already has a list of Laptops that a library has to lend out.
# Accepts user input to create a new Person - it should use the input function to read a person’s name, age, and preferred operating system.
# Tells the user how many laptops the library has that have that operating system.
# If there is an operating system that has more laptops available, tells the user that if they’re willing to accept that operating system they’re more likely to get a laptop.

# You should convert the age and preferred operating system input from the user into more constrained types as quickly as possible, 
# and should output errors to stderr and terminate the program with a non-zero exit code if the user input bad values.

# ----- Imports
from dataclasses import dataclass
from enum import Enum
import sys

 # ----- Classes and Enums
class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"
    WINDOWS = "Windows"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem

@dataclass(frozen=True)
class Laptop:
    id: int
    operating_system: OperatingSystem

 # ----- Functions
def count_laptops(laptops: list[Laptop], laptop_counts: dict[str, int]):
    for laptop in laptops:
        laptop_counts[laptop.operating_system] += 1 

def check_laptop_abundance(user: Person, laptop_counts: dict[OperatingSystem, int]):
    abundant_laptops = []
    for laptop in laptop_counts:
        if laptop_counts[laptop] > laptop_counts[user.preferred_operating_system]:
            abundant_laptops.append(laptop.value)
    if len(abundant_laptops) > 0:
        print("\nIf you are willing to accept another operating system you may get a laptop sooner.")
        print("We have more laptops available with the following OS:")
        for laptop in abundant_laptops:
            print(laptop)
            
 # ----- Data and Constants
laptops = [
    Laptop(id=1, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, operating_system=OperatingSystem.ARCH),
    Laptop(id=3, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=5, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=6, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=7, operating_system=OperatingSystem.MACOS),
    Laptop(id=8, operating_system=OperatingSystem.MACOS),
]
laptop_counts = {
    OperatingSystem.MACOS: 0,
    OperatingSystem.ARCH: 0,
    OperatingSystem.UBUNTU: 0,
    OperatingSystem.WINDOWS: 0
}

 # ----- Script
user_name = input("Please enter your full name:\n")
user_age_str = input("Please enter your age:\n")

try:
    user_age = int(user_age_str)
except ValueError:
    sys.exit("Error: Age should be a number.")

user_operating_system_str = input("Please enter your preferred operating system (options: ARCH, UBUNTU, MACOS, WINDOWS):\n")

if user_operating_system_str not in OperatingSystem.__members__:
    sys.exit("Error: Operating system should be written in all caps from given options.")
else: user_operating_system = OperatingSystem[user_operating_system_str]

user = Person(user_name, user_age, user_operating_system)

count_laptops(laptops, laptop_counts)
print(f"\nThe number of available laptops with {user_operating_system.value} is: {laptop_counts[user_operating_system]}")

check_laptop_abundance(user, laptop_counts)