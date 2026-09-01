# Write a Person class using @datatype which uses a datetime.date for date of birth, rather than an int for age.
from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Person:
    name: str
    dob: date
    preferred_operating_system: str

# Re-add the is_adult method to it.
    def is_adult(self):
        dob = self.dob
        today = date.today()
        if dob.year > today.year - 18: return False
        if dob.year == today.year - 18:
            if dob.month > today.month: return False
            if dob.month == today.month:
                if dob.day > today.day: return False
        return True


imran = Person("Imran", date(2004, 8, 31), "Ubuntu")
print(imran.is_adult())