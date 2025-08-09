import random

choices = ['Rock', 'Paper', 'Scissors']

while(True):
    computer_choice = random.choice(choices)
    player_choice = None

    print('\nOptions:\n1. Rock\n2. Paper\n3. Scissors')

    choice1 = input('Enter your choice (1 - 3): ')
    match(choice1):
        case '1':
            player_choice = 'Rock'
        case '2':
            player_choice = 'Paper'
        case '3':
            player_choice = 'Scissors'
        case _:
            print('Invalid Choice.')
            continue

    print(f'\nYour Choice: {player_choice}')
    print(f'Computer\'s Choice: {computer_choice}')


    if player_choice == computer_choice:
        print('Its a tie!')
    elif player_choice == 'Paper' and computer_choice == 'Rock':
        print('You Win!')
    elif player_choice == 'Rock' and computer_choice == 'Scissors':
        print('You Win!')
    elif player_choice == 'Scissors' and computer_choice == 'Paper':
        print('You Win!')
    else:
        print('You Lose!')

    choice2 = (input('\nPlay Again (Y/N) ? '))
    if choice2 == 'Y' or choice2 == 'y':
        continue
    else:
        break
    


    
