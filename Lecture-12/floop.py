numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def sum_even_squares(nums):
    total = 0
    for n in nums:
        square = n ** 2
        if square % 2 == 0:
            total += square
    return total

result = sum_even_squares(numbers)
print(result)  # Output: 220