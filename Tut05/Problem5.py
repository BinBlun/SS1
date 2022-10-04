import random

n = int(input("Please enter a number of throws: "))

def random_Number():
    randNumbers = []
    for number in range(0, n):
        number = random.randint(1, 6)
        randNumbers.append(number)
    return randNumbers

def main():
    print(f"Throw the dice {n} time(s) and the result is " + str(random_Number()))

main()
