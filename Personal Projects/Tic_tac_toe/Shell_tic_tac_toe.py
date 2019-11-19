
import random



# ALLOWS PLAYER TO CHOOSE DIFFICULTY #
def choose_difficulty():
    mode = input('Choose Difficulty: Easy   Hard  --->  ').upper()
    if mode == 'EASY' or mode == 'HARD':
        return mode
    else:
        print('invalid input')
        return choose_difficulty() 



# PRINTS BOARD IN CURRENT STATE #
def display_board(board):
    for i in range(3):
        print(' '.join(board[3*i:3*i+3]))
    print()



# DETERMINES IF EITHER PLAYER HAS WON OR DRAWN #
def winner(board):
    win_conditions = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],
                      [1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] and board[condition[0]] == board[condition[2]] and board[condition[0]] == 'X':
            return 'X'
        if board[condition[0]] == board[condition[1]] and board[condition[0]] == board[condition[2]] and board[condition[0]] == 'O':
            return 'O'
    if '-' in board:
        return '-'
    return 'D'



# RETURNS A LIST OF OPEN INDECIES #
def open_slots(board):
    empty_spaces = [] 
    for slot in range(len(board)):
        if board[slot] == '-': 
            empty_spaces.append(slot) 
    return empty_spaces




# DETERMINES IF THERE'S A MOVE THAT COULD LEAD TO A WIN #
def force_win(board):
    if len(open_slots(board)) % 2 == 0:
        player = 'O'
    else:
        player = 'X'
    if winner(board) != '-':
        if winner(board) == 'X':
            return 1
        if winner(board) == 'O':
            return -1
        if winner(board) == 'D':
            return 0
    else:
        if player == 'O':
            state = 1
            for i in open_slots(board):
                copy_board = list(board)
                copy_board[i] = player
                new_state = force_win(copy_board)
                if new_state < state:
                    state = new_state
            return state
        else:
            state = -1
            for i in open_slots(board):
                copy_board = list(board)
                copy_board[i] = player
                new_state = force_win(copy_board)
                if new_state > state:
                    state = new_state
            return state




# PLACES USER AND CPU PIECE #
def take_turn(board,mode):
        print('')
        display_board(board)
        spot = input('Where would you like to play? 1-9: ')
        if spot.isnumeric() == True:
            spot = int(spot) - 1
            if spot in open_slots(board):
                board[spot] = 'X'
            else:
                print('Please choose a valid location')
                return take_turn(board,mode)
        else:
            print('Please choose a valid location')
            return take_turn(board,mode)
        if winner(board) == '-':
            if mode == 'HARD':
                state = 1
                for i in open_slots(board):
                    copy_board = list(board)
                    copy_board[i] = 'O'
                    new_state = force_win(copy_board)
                    if new_state < state:
                        state = new_state
                        spot = i
                board[spot] = 'O'
                return board
            else:
                board[random.choice(open_slots(board))] = 'O'
                return board
        else:
            return board


# FOLLOWS THE PROCEDURE OF A TIC TAC TOE GAME #
def tic_tac_toe():
    mode = choose_difficulty()
    board = ['-'] * 9
    while winner(board) == '-':
        take_turn(board,mode)
    display_board(board)
    if winner(board) == 'X':
        print( 'You Win!' )
    if winner(board) == 'D':
        print( 'Almost!' )
    else:
        print( 'Better luck next time' )
    print('')
    rematch = input( 'Would you like to play again? ' )
    if rematch.isalpha() == True:
        rematch = rematch.upper()
        if rematch == 'YES':
            return tic_tac_toe()
        if rematch == 'NO':
            print('Thanks for playing!')
        else:
            print('invalid response. Game terminated')
    else:
        print('invalid response. Game terminated')

        
tic_tac_toe()
