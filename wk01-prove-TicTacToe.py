#      Tic-Tac-Toe
#Love is a game of tic-tac-toe,
#Constantly waiting for the next x or o.
#    - Lang Leav -

# requirement 1 - complete



v0 = [1, 2, 3, 
     4, 5, 6, 
     7, 8, 9]

v1 = [1, 2, 3, 
     4, 5, 6, 
     7, 8, 9]





def main():
# requirement 5 - complete - "main" function
    print()
    print("Let's play Tic-Tac-Toe!")
    print(f" {v0[0]} | {v0[1]} | {v0[2]}")
    print("-----------")
    print(f" {v0[3]} | {v0[4]} | {v0[5]}")
    print("-----------")
    print(f" {v0[6]} | {v0[7]} | {v0[8]}")
    print()
    
    game_end = False
    player = 'o'
    while game_end == False:
# requirement 3 - complete - while loop
        player = player_turn(player)
        game_end = game_check(v1)
        draw_board()
        

# requirement 4 - complete - more than one function
# 4 functions: main(), draw_board(), player_turn(), game_check()    

        





def draw_board():

    print()
    print(f" {v1[0]} | {v1[1]} | {v1[2]}")
    print("-----------")
    print(f" {v1[3]} | {v1[4]} | {v1[5]}")
    print("-----------")
    print(f" {v1[6]} | {v1[7]} | {v1[8]}")
    print()


def player_turn(player):
    # requirement 2 - complete - if/then block
    if player == 'x':
        print("Player X's turn...")
        x_play_raw = int(input('Which position do you claim? (1-9): '))
        x_play = x_play_raw - 1
        if v1[x_play] == v0[x_play]:
            v1[x_play] = 'x'
            
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
            
            player = 'x'
            return player
            

        else:
            print('try again, spot taken')
            player_turn(player)

    else: 
        print('error: exiting')
        game_end = True
        return game_end



def game_check(v1):

    #if      #player X wins


    #if      #player O wins


    if any(isinstance(x, int) for x in v1):     # if a DRAW, no winners
        game_end = False
        return game_end
    else: 
        game_end = True
        print('DRAW! Game over, no winners!')
        return game_end














if __name__ == '__main__':
    main()



