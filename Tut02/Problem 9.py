# get input
weight = float(input("Enter the weight of a package : "))
rate = str

# if else
if weight <= 2:
    rate = "$1.50"
elif weight <= 6:
    rate = "$3.00"
elif weight <= 10:
    rate = "$4.00"
else:
    rate = "$4.75"

# display result
print("The shipping charges : ", rate)
