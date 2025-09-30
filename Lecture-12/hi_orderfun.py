def apply_twice(func, arg):
    return func(func(arg))

def increment(x):
    return x + 1

print(apply_twice(increment, 5))  # Output: 7