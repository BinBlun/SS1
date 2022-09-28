# get the total square feet
totalSquareFeet = int(input('Input the total square feet: '))

# cal the total acres
totalAcre = totalSquareFeet / 43560

# show the total acre
print('The total Acres is:', format(totalAcre, ',.2f'))
