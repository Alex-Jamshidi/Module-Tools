import math
import random
from collections import Counter
from datetime import datetime

from laptop_allocation import Laptop, OperatingSystem, Person, allocate_laptops


# ----- Log and Print functions
def log(message, filename="log.txt"):
    with open(filename, "a") as f:
        f.write(f"{message}\n")


def log_and_print(message, filename="log.txt"):
    print(message)
    with open(filename, "a") as f:
        f.write(f"{message}\n")


# THIS CODE CLEARS THE LOG EACH RUN - COMMENT TO KEEP LOG HISTORY
with open("log.txt", "w") as file:
    pass


# ----- Data Functions
def create_people() -> list[Person]:
    people = []
    for i in range(number_of_people):
        people.append(
            Person(f"Person {i + 1}", random.randint(18, 99), get_preferred_OS_list())
        )

    print("List of people added to log.txt")
    log("\n===== List of People =====")

    for person in people:
        preferred_OS_list = []
        for OS in person.preferred_operating_systems:
            preferred_OS_list.append(OS.value)
        log(
            f"Name: {person.name} |  Age: {person.age} |  Preferred OS: {', '.join(preferred_OS_list)}"
        )

    return people


def get_preferred_OS_list() -> tuple[OperatingSystem, ...]:
    number_of_preferences = random.choices([1, 2, 3], OS_preference_weightings)
    return tuple(random.sample(list(OperatingSystem), k=number_of_preferences[0]))


def create_laptops() -> list[Laptop]:
    laptops = []
    for i in range(number_of_laptops):
        os = random.choices(list(OperatingSystem))[0]
        if os == OperatingSystem.MACOS:
            manufacturer = "Apple"
            model = "macBook"
        else:
            manufacturer = "Dell "
            model = "XPS    "
        screen_size = random.choices([13, 14, 15, 16, 17])[0]

        laptops.append(Laptop(i + 1, manufacturer, model, screen_size, os))

    print("\nList of laptops added to log.txt")
    log("\n===== List of Laptops =====")

    for laptop in laptops:
        log(
            f"ID: {laptop.id} |  Manufacturer: {laptop.manufacturer} |  Model: {laptop.model} |  Screen size (inches): {laptop.screen_size_in_inches} |  OS: {laptop.operating_system.value}"
        )

    return laptops


def count_operating_systems(list_of_laptops: list[Laptop]) -> dict[str, int]:
    counts = Counter(laptop.operating_system.value for laptop in list_of_laptops)
    sorted_counts = dict(sorted(counts.items(), key=lambda item: item[0]))

    log("\nLaptop operating system options:")
    for os_name, count in sorted_counts.items():
        log(f"{os_name}: {count}")
    return sorted_counts


def count_first_choice_operating_systems(
    list_of_people: list[Person],
) -> dict[str, int]:
    counts = Counter(
        person.preferred_operating_systems[0].value for person in list_of_people
    )
    sorted_counts = dict(sorted(counts.items(), key=lambda item: item[0]))

    log("\nFirst choice of operating systems:")
    for os_name, count in sorted_counts.items():
        log(f"{os_name}: {count}")
    return sorted_counts


def count_second_choice_operating_systems(
    list_of_people: list[Person],
) -> dict[str, int]:
    counts = Counter(
        person.preferred_operating_systems[1].value
        for person in list_of_people
        if len(person.preferred_operating_systems) > 1
    )

    sorted_counts = dict(sorted(counts.items(), key=lambda item: item[0]))

    log("\nSecond choice of operating systems:")
    for os_name, count in sorted_counts.items():
        log(f"{os_name}: {count}")
    return sorted_counts


def count_third_choice_operating_systems(
    list_of_people: list[Person],
) -> dict[str, int]:
    counts = Counter(
        person.preferred_operating_systems[2].value
        for person in list_of_people
        if len(person.preferred_operating_systems) > 2
    )

    sorted_counts = dict(sorted(counts.items(), key=lambda item: item[0]))

    log("\nThird choice of operating systems:")
    for os_name, count in sorted_counts.items():
        log(f"{os_name}: {count}")
    return sorted_counts


def get_sadness_scores(allocations: dict[Person, Laptop]) -> dict[int, int]:
    sadness_scores = {0: 0, 1: 0, 2: 0, 100: 0}
    for person, laptop in allocations.items():
        try:
            sadness_score = person.preferred_operating_systems.index(
                laptop.operating_system
            )
        except ValueError:
            sadness_score = 100
        sadness_scores[sadness_score] += 1
    return sadness_scores


def calculate_total_sadness(scores: dict[int, int]) -> int:
    total_sadness = 0
    if laptop_surplus < 0:
        total_sadness += -laptop_surplus * 100
    for score, occurrence in scores.items():
        total_sadness += score * occurrence
    return total_sadness


# ----- Random Simulation
log_and_print("-------------------------------------------")
log_and_print(f"Simulation created at: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
log_and_print("-------------------------------------------")

laptop_to_person_weighting = random.uniform(0.5, 2)
log_and_print(f"Laptop to person weighting = {laptop_to_person_weighting:.2f}")

number_of_people = random.randint(10, 100)
log_and_print(f"Number of People: {number_of_people}")

number_of_laptops = math.floor(number_of_people * laptop_to_person_weighting)
log_and_print(f"Number of Laptops: {number_of_laptops}")

laptop_surplus = number_of_laptops - number_of_people
log(f"\nLaptop surplus/deficit: {laptop_surplus}\n")

number_of_available_OS = 3
OS_preference_weightings = []

for i in range(number_of_available_OS):
    OS_preference_weightings.append(random.random())

sum_of_OS_preference_weightings = sum(OS_preference_weightings)

for i in range(number_of_available_OS):
    percentage_chance = (
        OS_preference_weightings[i] / sum_of_OS_preference_weightings
    ) * 100
    log_and_print(f"Percentage chance of {i + 1} preference: {percentage_chance:.2f}%")

laptops = create_laptops()
people = create_people()

count_operating_systems(laptops)
count_first_choice_operating_systems(people)
count_second_choice_operating_systems(people)
count_third_choice_operating_systems(people)

allocated_laptops = allocate_laptops(people, laptops)
print("List of allocations added to log.txt")

sadness_scores = get_sadness_scores(allocated_laptops)
log_and_print(f"\nFirst choice OS given: {sadness_scores[0]}")
log_and_print(f"Second choice OS given: {sadness_scores[1]}")
log_and_print(f"Third choice OS given: {sadness_scores[2]}")

log_and_print(
    f"\n>>>>> Total Sadness Score: {calculate_total_sadness(sadness_scores)} <<<<<"
)

if number_of_people > number_of_laptops:
    log_and_print(
        f"\nNote: Due to a deficit of {-laptop_surplus} laptops, the minimum sadness score theoretically achievable could never be less than {-laptop_surplus * 100}"
    )


log("\n===== Allocations =====")
for person, laptop in allocated_laptops.items():
    preferred_OS = ""
    for OS in person.preferred_operating_systems:
        preferred_OS += OS.value + " | "
    log(f"{person.name} -- Preferred OS: {preferred_OS[:-2]}")
    log(f"----> Laptop ID: {laptop.id} -- OS: {laptop.operating_system.value}\n")
