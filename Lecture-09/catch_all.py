try:
    value = int(input("Enter a number: "))
    result = 10 / value
except Exception as e:
    print("Error:", e)

print("End of the program")