fat = int(input("Please input the fat gram you consume: "))
crabs = int(input("Please input the crabs gram you consume: "))

caloFromFat = fat * 9
caloFromCrabs = crabs * 4

print("The number of calories that result from the fat is: " + str(caloFromFat))
print("The number of calories that result from the crabs is: " + str(caloFromCrabs))
print("The total calories is: " + str(caloFromFat + caloFromCrabs))
