import json
import pickle
MENU = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
vegetable_library = {'cucumber':'2.00','tomato':'1.00','cabbage':'0.99','potato': '1.50'}

with open('vegetable.txt','w') as convert_file:
       convert_file.write(json.dumps(vegetable_library))

with open('vegetable.txt') as json_file:
    data = json.load(json_file)

def main():
    choice = 0
    while choice != QUIT:
        choice = getMenuChoice()
        if choice == MENU:
            menu(data)
        elif choice == ADD:
            add(data)
        elif choice == CHANGE:
            change(data)
        elif choice == DELETE:
            delete(data)
        else:
            exit

def getMenuChoice():
    print()
    print('Name and Email Address Catalog')
    print('------------------------------')
    print('1. See all the menu')
    print('2. Add a new vegetable')
    print('3. Change a vegetable')
    print('4. Delete a vegetable')
    print('5. Quit the program')
    print()

    choice = int(input('Enter the choice: '))
    while choice < MENU or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    return choice

def menu(vegetable):
    vegetable_library_items = vegetable.items()
    for item in vegetable_library_items:
        print(item)

def add(vegetable):
    name = input("Enter a new name vegetable: ")
    price = input("Enter a price: ")
    if name not in vegetable:
        vegetable[name] = price
        with open("vegetable.txt", "wb") as infile:
            pickle.dump(vegetable, infile)
    else:
        print('That vegetable has already exists.')

def change(vegetable):
    name = input("Enter a name vegetable: ")
    if name in vegetable:
        price = input("Enter a new price: ")
        vegetable[name] = price
        with open("vegetable.txt", "wb") as infile:
            pickle.dump(vegetable, infile)
    else:
        print('That name is not found.')

def delete(vegetable):
    name = input('Enter a name vegetable: ')
    if name in vegetable:
        del vegetable[name]
    else:
        print('That name is not found.')

main()
