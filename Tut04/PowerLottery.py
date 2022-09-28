import random

print("Enter 5 different numbers from 1 to 69")
userNumber = []

for i in range(5):
    userNumber.append(int(input("=> ")))
userNumber.sort()

print("Enter number from 1 to 26")
powerBall = int(input("=> "))

possibleNumbers = list(range(1, 70))
random.shuffle(possibleNumbers)
winNumbers = possibleNumbers[0:5]
winNumbers.sort()
winPowerBall = random.randint(1, 26)

allWinNumbers = 'The winning numbers are: '
for i in range(5):
    allWinNumbers += str(winNumbers[i]) + ' '
allWinNumbers += 'and the winning POWERBALL is: ' + str(winPowerBall)
print(allWinNumbers)

if(set(winNumbers) == set(userNumber) and powerBall == winPowerBall):
    print("You won")
else:
    print("You lose")


