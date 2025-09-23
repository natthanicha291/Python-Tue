class Dog:
    species = 'mammal'
    def calAge(self, age):
        print('Dog age is {}'.format(age * 3))

class SomeBreed(Dog):
    pass

class SomeOtherBreed(Dog):
    species = 'canine'
    def calAge(self, age):
        print('Dog age is {}'.format(age * 4))

frank = SomeBreed()
print(frank.species)
frank.calAge(5)

beans = SomeOtherBreed()
print(beans.species)
beans.calAge(5)