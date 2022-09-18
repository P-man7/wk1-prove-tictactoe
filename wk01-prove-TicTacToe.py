#      Tic-Tac-Toe
#Love is a game of tic-tac-toe,
#Constantly waiting for the next x or o.
#    - Lang Leav -

from multiprocessing.pool import TERMINATE
from pytest import ExitCode


v0 = [1, 2, 3, 
     4, 5, 6, 
     7, 8, 9]

v1 = [1, 2, 3, 
     4, 5, 6, 
     7, 8, 9]





def main():

    print()
    print("Let's play Tic-Tac-Toe!")
    print(f" {v0[0]} | {v0[1]} | {v0[2]}")
    print("-----------")
    print(f" {v0[3]} | {v0[4]} | {v0[5]}")
    print("-----------")
    print(f" {v0[6]} | {v0[7]} | {v0[8]}")
    print()
    
    game_end = False
    player = 'x'
    while game_end == False:

        player = player_turn(player)
        





def draw_board():

    print()
    print(f" {v1[0]} | {v1[1]} | {v1[2]}")
    print("-----------")
    print(f" {v1[3]} | {v1[4]} | {v1[5]}")
    print("-----------")
    print(f" {v1[6]} | {v1[7]} | {v1[8]}")
    print()


def player_turn(player):
    if player == 'x':
        print("Player X's turn...")
        x_play_raw = int(input('Which position do you claim? (1-9): '))
        x_play = x_play_raw - 1
        if v1[x_play] == v0[x_play]:
            v1[x_play] = 'x'
            print(v1)
            player = 'o'
            return player
            

        else:
            print('try again, spot taken')
            player_turn(player)

    if player == 'o':
        print("Player O's turn...")
        o_play_raw = int(input('Which position do you claim? (1-9): '))
        o_play = o_play_raw - 1
        if v1[o_play] == v0[o_play]:
            v1[o_play] = 'o'
            print(v1)
            player = 'x'
            return player
            

        else:
            print('try again, spot taken')
            player_turn(player)

    else: 
        print('error: exiting')
        TERMINATE
















if __name__ == '__main__':
    main()



