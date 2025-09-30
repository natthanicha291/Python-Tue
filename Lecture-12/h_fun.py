def apply_funtion(func, value):
    return func(value)

def square(x):
    return x * x

def increment(x):
    return x + 1

print(apply_funtion(square, 5)) #output: 25
print(apply_funtion(increment, 5)) #output: 6