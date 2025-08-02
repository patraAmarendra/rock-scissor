import random

def choseOptions():
    print('Welcome to Rock, Scissor, Paper game!')
    print('Please choose one of the following options:')
    options = ('rock', 'scissor', 'paper')
    for i, option in enumerate(options,1):
        print(f'{i}. {option}')
    while True:
        player = input().lower().strip()
        if player in ["1","2", "3"]:
            if player == "1":
                player = "rock"
                break
            elif player == "2":
                player = "scissor"
                break
            elif player == "3":
                player = "paper"
                break
        elif player not in options:
            print(f'Invalid option, {player} is not a valid choice. Please choose from {options}.')
        else:
            break
    computer = random.choice(options)
    return player, computer


def checkWinner(player, computer):
    if player == computer:
        return 'Its a tie'
    elif player == 'rock':
        if computer == 'scissor':
            return 'Rock crashes scissor. You win!'
        else:
            return 'Paper covers rock. You lose!'
    elif player == 'scissor':
        if computer == 'paper':
            return 'Scissor cuts paper. You win!'
        else:
            return 'Rock crashes scissor. You lose!'
    elif player == 'paper':
        if computer == 'rock':
            return 'paper cover rock.You win!'
        else:
            return 'Scissor cuts paper. You lose!'
        
value = choseOptions()
print(f'You chose: {value[0]} and computer chose: {value[1]}')
print(checkWinner(value[0], value[1]))