squareFeetOfWallSpace = int(input("Please input the square feet of wall space: "))

gallonNeeds = squareFeetOfWallSpace/112
timeNeeds = (squareFeetOfWallSpace/112)*8

laborSalary = 35 * timeNeeds;

print("The number of gallons of paint required: ", gallonNeeds)
print("The hours of labor required: ", timeNeeds)
print("The labor charges: ", laborSalary)
