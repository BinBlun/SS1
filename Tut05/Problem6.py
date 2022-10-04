input1 = open('BoyNames.txt').read().split()
input2 = open('GirlNames.txt').read().split()

user_input = input("Please enter a boy’s name or a girl’s name: ")

def check_for_name(name):
    a = name.capitalize()
    if a in input1:
        return print("The name is one of the most popular boy's name")
    elif a in input2:
        return print("The name is one of the most popular girl's name")
    else:
        return print("The name is NOT one of the most popular boy's or girl's name")

def main():
    check_for_name(user_input)

main()
