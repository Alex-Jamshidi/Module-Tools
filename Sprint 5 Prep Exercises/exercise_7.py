from datetime import date

class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str, dob: date):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system
        self.dob = dob

    def is_adult(self):
        dob = self.dob
        today = date.today()
        if dob.year > today.year - 18: return False
        if dob.year == today.year - 18:
            if dob.month > today.month: return False
            if dob.month == today.month:
                if dob.day > today.day: return False
        return True


imran = Person("Imran", 22, "Ubuntu", date(2004, 8, 31))
print(imran.is_adult())

# Change the Person class to take a date of birth
# (using the standard library’s datetime.date class) and store it in a field instead of age.

# Update the is_adult method to act the same as before.