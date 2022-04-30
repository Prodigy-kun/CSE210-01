board = [ '1','2','3','4','5','6','7','8','9']
players = ['x','o']

def main():
    play = verify_input(f'Enter a number from (1-9)', 9, 1)
    play = f'{play}'


def winning(board):
     return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])
        

def make_move(play):
    if play in board:
        play_index = board.index(play)
        board[play_index] = 'X'
        print_board(board)
    else:
        print('position unavailable, choose anoher!.')
        play = str(verify_input(f'Enter a number from (1-9)', 9, 1))
        make_move(play)
        



def print_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()


def verify_input(prompt, upper_bound, lower_bound):
    while True:
        try:
            play = int(input(prompt))
            if play > upper_bound:
                print('Error: input too high, enter a number from 1-9')
            elif play < lower_bound:
                print('Error: input too low, enter a number from 1-9')
            else:
                break
            
        except ValueError as val_err:
            print('Error: You entered a number that is not recognized, please enter another.')
    return play


# main()
make_move('10')