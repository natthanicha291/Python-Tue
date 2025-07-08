inchar = input("input your character: ")
if inchar >= 'A' and inchar <= 'Z':
    print("Upper case Letter")
elif inchar >= 'a' and inchar <= 'z':
    print("Loewer case Letter")
elif inchar >= '0' and inchar <= '9':
    print("Number")
else :
    print("Special Character",inchar)