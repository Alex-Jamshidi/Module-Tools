class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
print(imran.address)

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
print(eliza.address)

# exercise_4_and_5.py:9: error: "Person" has no attribute "address"  [attr-defined]
# exercise_4_and_5.py:13: error: "Person" has no attribute "address"  [attr-defined]
# Found 2 errors in 1 file (checked 1 source file)

# There is no address attribute for a Person, only name, age and preferred operating system.

# Add the is_adult code to the file you saved earlier.
def is_adult(person: Person) -> bool:
    return person.age >= 18

print(is_adult(imran))

# Run it through mypy - notice that no errors are reported - 
# mypy understands that Person has a property named age so is happy with the function.

def is_banana(person: Person) -> bool:
    return person.banana

print(is_banana(imran))

# exercise_4_and_5.py:31: error: "Person" has no attribute "banana"  [attr-defined]