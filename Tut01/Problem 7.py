#the total purchase
totalPurchase = float(input('Input the total amount of purchase: '))

#cal the state sales tax(5%)
stateTax = totalPurchase * 0.05

#cal the county sales tax(2.5%)
countyTax = totalPurchase * 0.025

#cal the total sales
totalSale = (totalPurchase + stateTax + countyTax)

#display the total purchase
print('Amount of the purchase :', format(totalPurchase, ',.2f'))

#display the state sales tax
print('Amount of the state sales tax :', format(stateTax, ',.2f'))

#display the county sales tax
print('Amount of the county sales tax :', format(countyTax, ',.2f'))

#display the total sales
print('total sales :', format(totalSale, ',.2f'))
