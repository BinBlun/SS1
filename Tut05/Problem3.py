def user_enter_numbers():
    try:
        numbers = []
        index = 1
        for i in range(0,20):
            number = float(input(f"Please input {index} number: "))
            numbers.append(number)
            index += 1
        return numbers
    except ValueError:
        print('Please enter a number')

def calculateTotal(numbers):
    total_rainfall = 0
    for number in numbers:
        total_rainfall += number
    return total_rainfall

def calculateAverage(numbers):
    total_numbers = 0
    for number in numbers:
        total_numbers += number
    average_numbers = total_numbers/12;
    return average_numbers

def theHighest(numbers):
    return max(numbers)

def theLowest(numbers):
    return min(numbers)

def main():
    numbers = user_enter_numbers()
    print("Total: " + str(calculateTotal(numbers)))
    print("The average: " + str(calculateAverage(numbers)))
    print("The highest number: " + str(theHighest(numbers)))
    print("The lowest number: " + str(theLowest(numbers)))

main()
