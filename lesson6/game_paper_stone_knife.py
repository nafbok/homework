import random
def game(*setGame):
    player = input('Player, enter your figure: ')
    pc_imput = random.choice(list(setGame))
    print('PC entered: ', pc_imput)
    if str(pc_imput) == str(player):
        print('Draw')
    for i in setGame:
        if pc_imput == setGame[0] and player == setGame[1] or player == setGame[2]:
            print('PC - win')
        elif player == setGame[0] and pc_imput == setGame[1] or pc_imput == setGame[2]:
            return 'Player - win'
        elif pc_imput == setGame[2] and player == setGame[1]:
            return 'PC - win'
        elif player == setGame[2] and pc_imput == setGame[1]:
            return 'Player - win'
print(game('rock', 'paper', 'siccers'))