g = 9.8
def fallingDistance(fallingTime):
    return 0.5 * g * (fallingTime ** 2)

for i in range(11):
    d = fallingDistance(i + 1)
    print("The distance fall in " + str(i) + " second is: " + str(round(d, 2)))
