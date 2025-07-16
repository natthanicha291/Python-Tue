def print_args(*args):
    for index, arg in enumerate(args):
        print(f"Argument {index + 1}: {arg}")

print_args("Python", 3.8, True, [1, 2, 3], {"key": "value"})