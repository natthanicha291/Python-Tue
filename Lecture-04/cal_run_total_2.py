max = 5

total = 0.0

print('This program calculates the sum of')
print(max,'numbers you will emter')

for counter in range(max):
    number = int(input('Enter a number: '))
    total = total + number

print('The total is', total)