class parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
blu = parrot("blu", 15)
polly = parrot("polly", 10)

print("blu is a", blu.species)
print("polly is a", polly.species)

print("blu is", blu.age, "years old.")
print("polly is", polly.age, "years old.")