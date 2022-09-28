print("please input the actual value: ")
value = int(input())

assessmentValue = value * 0.6
print("Assessment value is $" + str(assessmentValue))

tax = (assessmentValue/100) * 0.72
print("Property tax is $", round(tax, 2))

