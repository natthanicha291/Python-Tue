animals = ["cat", "dog", "rabbit", "hamster", "dog", "parrot"]
first_dog_index = animals.index("dog")
print(f"First 'dog' index: {first_dog_index}")

second_dog_index = animals.index("dog", first_dog_index + 1)
print(f"Second 'dog' index: {second_dog_index}")