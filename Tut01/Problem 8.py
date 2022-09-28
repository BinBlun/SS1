#The number of miles
milesDriven = float(input('Input the number of miles driven : '))

#Get the gallons of gas used
gasUsed = int(input('Enter the gallons of gas used : '))

#calculate the MPG
mpg = milesDriven * gasUsed

#display the car’s MPG
print('cars MPG :', format(mpg, ',.2f'))
