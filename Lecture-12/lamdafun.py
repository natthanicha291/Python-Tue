from functools import reduce
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

filtered = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered)  # Output: [2, 4]

sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15 from functools import reduce