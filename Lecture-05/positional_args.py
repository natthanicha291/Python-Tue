def print_all(*arges):
    for index, arg in enumerate(arges):
        print(f"Argument {index + 1}: {arg}")

print_all("Python",3.8,True, [1, 2, 3], {"key": "value"})