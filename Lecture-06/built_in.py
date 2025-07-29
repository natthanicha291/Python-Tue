numbers = [4, 2, 9, 1, 5, 6]
lenght = len(numbers)
print(f'Length of the list: {lenght}')

total_sum = sum(numbers)
print(f'Sum of the list: {total_sum}')

max_value = max(numbers)
print(f'Maximum value in the list: {max_value}')

min_value = min(numbers)
print(f'Minimum value in the list: {min_value}')

sorted_numbers = sorted(numbers)
print(f'Sorted list: {sorted_numbers}')

bool_list = [False, True, False]
any_true = any(bool_list)
print(f'Any True in the list: {any_true}')

all_true = all(bool_list)
print(f'All True in the list: {all_true}')

string = "hello"
char_list = list(string)
print(f'List from string: {char_list}')

reversed_numbers = list(reversed(numbers))
print(f'Reversed list: {reversed_numbers}')

enumerated_numbers = list(enumerate(numbers))
print(f'Enumerated list: {enumerated_numbers}')