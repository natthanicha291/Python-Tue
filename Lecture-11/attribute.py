class Dog:
    species = 'mammal'  # Class attribute
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
 
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

print(f"{dog1.name} is a {dog1.species} and is {dog1.age} years old.")
print(f"{dog2.name} is a {dog2.species} and is {dog2.age} years old.")

if dog1.species == 'mammal':
    print(f"{dog1.name} is a mammal.")