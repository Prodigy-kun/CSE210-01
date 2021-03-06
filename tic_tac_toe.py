board = [ '1','2','3','4','5','6','7','8','9']

def main():
    player = next_player("")
    while not (winning(board) or is_a_draw(board)):
        print_board(board)
        make_move(player, board)
        player = next_player(player)
    print_board(board)
    if (winning(board)and player == 'x') or (winning(board) and player == 'o'):
        print(f"Good game, player {next_player('x')} Wins. Thanks for playing!") 
    elif is_a_draw(board):
        print("It's a draw!")


def make_move(player, board):
    square = verify_input(f"{player}'s turn to choose a square (1-9): ", 9, 0)
    board[square - 1] = player


def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True

def winning(board):
     return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

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

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"
main()