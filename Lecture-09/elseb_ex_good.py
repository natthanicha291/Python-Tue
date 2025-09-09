def davide(a,b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Error:", e)
    else:
        return result
    
a,b = map(int, input().split())
print(davide(a,b))
print("End of the program")