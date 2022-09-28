totalSale = int(input("Please input total sales of the month: "))

stateSalesTax = totalSale * 0.05;
countySalesTax = totalSale * 0.25;

print("The amount of county sales tax: ", stateSalesTax)
print("The amount of state sales tax: ", countySalesTax)
print("The total sale tax: ", stateSalesTax + countySalesTax)

