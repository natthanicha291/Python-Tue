test1 = float(input("Input test score 1: "))
test2 = float(input("Input test score 2: "))
test3 = float(input("Input test score 3: "))

average = (test1 + test2 + test3) / 3
print("the average score is: ",average)

if average > 95:
    print("Congratulation!")