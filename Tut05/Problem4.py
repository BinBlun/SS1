import random


def list_random_Number():
    randNumbers = []
    for number in range(1, 20):
        number = random.randint(0, 20)
        randNumbers.append(number)
    return randNumbers


def larger_than_n(listOfNumber):
    bigger_than_n = []
    n = int(input("Please input a number: "))
    for number in listOfNumber:
        if number > n:
            bigger_than_n.append(number)
    return bigger_than_n

def main():
    listOfNumber = list_random_Number()
    print(listOfNumber)
    print(larger_than_n(listOfNumber))

main()
