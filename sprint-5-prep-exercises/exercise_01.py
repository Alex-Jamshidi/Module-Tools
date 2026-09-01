# Exercise
# Predict what double("22") will do. 
# It will treat "22" as a integer and return 11 as an integer 

# Then run the code and check. 
def double(value):
    return value * 2

print(double("22"))

# Did it do what you expected? Why did it return the value it did?
# No, it treated it like a string, so instead of trying to do math, it did string repetition.