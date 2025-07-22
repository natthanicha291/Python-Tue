import random

HEADS = 1
TALLS = 2
TOSSES = 10

def main():
    for toss in range(TOSSES):
        if random.randint(HEADS, TALLS) == HEADS:
            print("Heads")
        else:
            print("Tails")

main()