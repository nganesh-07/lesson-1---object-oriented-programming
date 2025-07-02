class dog:
    breed1 = "golden lab"
    breed2 = "pomeranian"
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

mia = dog("pomeranian", 5)
nala = dog("golden lab", 8)

print("mia is a", dog.breed1)
print("nala is a", dog.breed2)

print("mia is", mia.age, "years old.")
print("nala is", nala.age, "years old.")