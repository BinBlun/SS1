numberAClass = int(input("Please input the number of ticket A class: "))
numberBClass = int(input("Please input the number of ticket B class: "))
numberCClass = int(input("Please input the number of ticket C class: "))

AClassSale = numberAClass * 20
BClassSale = numberBClass * 15
CClassSale = numberCClass * 10

print("The number of ticket A class: ", numberAClass)
print("The number of ticket B class: ", numberBClass)
print("The number of ticket C class: ", numberCClass)
print("-----------------------")
print("The income of A class: ", AClassSale)
print("The income of B class: ", BClassSale)
print("The income of C class: ", CClassSale)
print("The total of all class: ", AClassSale + BClassSale + CClassSale)


