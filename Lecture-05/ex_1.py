def is_armstrong(number):
    num_str = str(number)
    num_digis = len(num_str)
    total = 0

    for digit in num_str:
        total += int(digit) ** num_digis

    return total == number

print(is_armstrong(153))
print(is_armstrong(9474))
print(is_armstrong(123))