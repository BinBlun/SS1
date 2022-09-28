# formula : weight = mass × 9.8

# get input
mass = float(input("Enter an objects mass: "))

# calculate weight
weight = mass * 9.8

# if else
if weight > 500:
    print("It is too heavy")
elif weight < 100:
    print("It is too light")
