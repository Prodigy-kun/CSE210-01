board = [
    ['1','2','3'],
    ['+-+-'],
    ['4','5','6'],
    ['+-+-'],
    ['7','8','9']
]
i = 1
prompt = f'Player {i}, enter a number between (1-9)'
def main():
    pass

def verify_input(prompt, upper_bound, lower_bound):
    while True:
        try:
            play = input(prompt)
            if play > upper_bound:
                print('Error: input too high, enter a number from 1-9')
            elif play < lower_bound:
                print('Error: input too low, enter a number from 1-9')
        except ValueError as val_err:

            

# for i in range(0,len(board),2):
#     line = board[i]
#     for num in line:
#         print(num, end= '|')
#     print()
#     print('+-+-')
# for line in board:
#     for num in line:
#         print(num,end='|')
#     print()


if __name__ == '__main__':
    main()