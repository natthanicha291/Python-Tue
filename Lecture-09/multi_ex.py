try:
    value = int(input("Enter a number: "))
    result = 10 / value
    print(f"Result is {result}")
except ValueError:
    print("invalid input! Please enter a number.")
except ZeroDivisionError:
    print("cannot divide by zero!")

print("End of the program")