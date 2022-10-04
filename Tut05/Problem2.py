def user_enter_rainfall():
    try:
        rainIn12Month = []
        index = 1
        for i in range(0,12):
            numbers = float(input(f"Please input range rainfall in month {index}: "))
            rainIn12Month.append(numbers)
            index += 1
        return rainIn12Month
    except ValueError:
        print('Please enter a number')

def calculateTotalRainfall(rainfall):
    total_rainfall = 0
    for rainfall in rainfall:
        total_rainfall += rainfall
    return total_rainfall

def calculateAverageRainfall(rainfall):
    total_rainfall = 0
    for rainfall in rainfall:
        total_rainfall += rainfall
    average_rainfall = total_rainfall/12;
    return average_rainfall

def theHighest(rainfall):
    return max(rainfall)

def theLowest(rainfall):
    return min(rainfall)

def main():
    rainIn12Month = user_enter_rainfall()
    print("Total rainfall for the year: " + str(calculateTotalRainfall(rainIn12Month)))
    print("The average monthly rainfall: " + str(calculateAverageRainfall(rainIn12Month)))
    print("The highest month amount: " + str(theHighest(rainIn12Month)))
    print("The lowest month amount: " + str(theLowest(rainIn12Month)))

main()
