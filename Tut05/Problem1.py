import random

def random_Number():
    randNumbers = []
    for number in range(1, 8):
        number = random.randint(0, 9)
        randNumbers.append(number)
    return randNumbers

def display_numbers(random_numbers):
    print("Lottery number is ", end='')
    for random_number in random_numbers:
        print(str(random_number), end='')
    print('')


# define the main function
def main():
    # call random generator:
    randNumber = random_Number()
    # display the numbers:
    display_numbers(randNumber)

main()
while True:
    print("Do you want continue? (Y/N)")
    try:
        answer = input("=> ")
        if (answer == 'Y'):
            main()
        elif(answer == 'N'):
            break
    except ValueError:
        print('Please enter only Y/N')
        continue


