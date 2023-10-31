import random

x = ['Rock', 'Paper', 'Scissors']
computer = x[random.randint(0, 2)]

player = False

while player == False:
    player = input('Rock, Paper, Scissors ? ')
    if player == computer:
        print('Tie!')

    elif player == 'Rock':
        if computer == 'Paper':
            print('Computer covers player')
        else:
            print('player smashes computer')

    elif player == 'Paper':
        if computer == 'Scissors':
            print('player is cut')
        else:
            print('player covers computer')

    elif player == 'Scissors':
        if computer == 'Rock':
            print('computer breaks player')
        else:
            print('player cuts computer')

    else:
        print('You have typed a wrong term, try again!')

    player = False
    computer = x[random.randint(0, 2)]



