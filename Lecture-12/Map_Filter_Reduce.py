from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared = map(lambda x: x ** 2, numbers)
print(squared)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_numbers = filter(lambda x: x % 2 == 0, squared)
print(even_numbers)  # Output: [4, 16, 36, 64, 100]

sum_of_squares = reduce(lambda x, y: x + y, even_numbers)
print(sum_of_squares)  # Output: 220