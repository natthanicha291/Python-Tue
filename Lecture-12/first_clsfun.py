def greet (name):
    return f"Hello, {name}!"

say_hello = greet
print(say_hello("Alice"))  # Output: Hello, Alice!
print(greet("Bob"))        # Output: Hello, Bob!
# Both calls work the same way