employees = int(input("Number of employes: "))
if employees < 50:
    print("Small Company")
elif employees < 250:
    print("Medium Company")
elif employees >= 250:
    print("Large Company")