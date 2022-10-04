def main():
    right = 0
    wrong = 0
    capitals = {'VietNam': 'Hanoi', 'ThaiLand': 'Bangkok'}

    for i in capitals.keys():
        state = input('Enter the capital of '+ i +' :')
        if state.upper() == capitals[i].upper():
            right += 1
            print('Correct')
        else:
            wrong += 1
            print('Incorrect')

    print('Number of correct answers is: ', right)
    print("Number of incorrect answers is:", wrong)

    choice = input('Do you want to play again y/n: ')
    if choice.upper() == 'N':
        print('You suck!!!!')
    elif choice.upper() == 'Y':
        main()

main()
