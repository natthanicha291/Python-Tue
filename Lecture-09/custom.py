class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative number error: {value} is not allowed.")

def check_positive(number):
    if number < 0:
        raise NegativeNumberError(number)
    else:
        print(f"{number} is a positive number.")

try:
    num = int(input("Enter a positive number: "))
    check_positive(num)
except NegativeNumberError as e:
    print(e)
except ValueError:
    print("Invalid input! Please enter an integer.")
finally:
    print("Execution completed.")
print("End of the program")