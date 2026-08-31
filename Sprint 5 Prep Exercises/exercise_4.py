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

# exercise_4.py:9: error: "Person" has no attribute "address"  [attr-defined]
# exercise_4.py:13: error: "Person" has no attribute "address"  [attr-defined]
# Found 2 errors in 1 file (checked 1 source file)

# There is no address attribute for a Person, only name, age and preferred operating system.