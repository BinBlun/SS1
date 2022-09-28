import random

num1 = random.randint(1, 1000)
num2 = random.randint(1, 1000)
total = num1 + num2
print(num1, '+', num2)
userAnswer = int(input("What is the answer: "))
print("Your answer is: ", total == userAnswer)

