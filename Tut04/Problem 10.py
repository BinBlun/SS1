moneyInAccount = int(input("Please input the money you want to saving: "))
numberOfMonth = int(input("Please input the number of month you want to: "))

if numberOfMonth <= 3:
    print("Your interest rate is: 4.4%")
    print("Your future value is: " + str(round(moneyInAccount * (1 + 0.044) * numberOfMonth,2)) + "$")
elif numberOfMonth > 3 and numberOfMonth < 6:
    print("Your interest rate is: 4.7%")
    print("Your future value is: " + str(round(moneyInAccount * (1 + 0.047) * numberOfMonth,2)) + "$")
elif numberOfMonth >= 6 and numberOfMonth < 9:
    print("Your interest rate is: 5%")
    print("Your future value is: " + str(round(moneyInAccount * (1 + 0.05) * numberOfMonth,2)) + "$")
elif numberOfMonth >= 9 and numberOfMonth < 12:
    print("Your interest rate is: 5.1%")
    print("Your future value is: " + str(round(moneyInAccount * (1 + 0.051) * numberOfMonth,2)) + "$")
elif numberOfMonth >= 12:
    print("Your interest rate is: 6.7%")
    print("Your future value is: " + str(round(moneyInAccount * (1 + 0.067) * numberOfMonth,2)) + "$")
