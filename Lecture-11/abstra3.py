class Dog:
    species = 'mammal'
    def calAge(self, age):
        print('Your dog age is:', age*7)

class SomeBreed(Dog):
    pass

class SomeOtherBreed(Dog):
    species = 'Canine'
    def calAge(self, age):
        print('Your dog age is:', age*8)

frank = SomeBreed()
print(frank.species)
frank.calAge(5)

beans = SomeOtherBreed()
print(beans.species)
beans.calAge(5)