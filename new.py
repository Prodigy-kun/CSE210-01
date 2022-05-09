# # board = [
# #     ['1','2','3'],
    
# #     ['4','5','6'],
    
# #     ['7','8','9']
# # ]

# def main():
#     play = verify_input(f'Player , enter a number between (1-9)', 9, 1)
#     play = f'{play}'
#     # for row in board:
#     #     for lines in row:
#     #         if play == lines:
#     #             lines = 'x'
#     #             # play_i = row.index(play)
#     #         # row[play_i] = 'x'
#     #         make_board(board)
#     while True:
#         for row in board:
#             if play in row:
#                 play_i = row.index(play)
#             row[play_i] = 'x'
#             break
#         make_board(board)
#         return True
       

        

# def make_board(board):
#     for row in board:
#         for num in row:
#             print(num, end='|')
#         print()
#         print('-+-+-')

# def verify_input(prompt, upper_bound, lower_bound):
#     while True:
#         try:
#             play = int(input(prompt))
#             if play > upper_bound:
#                 print('Error: input too high, enter a number from 1-9')
#             elif play < lower_bound:
#                 print('Error: input too low, enter a number from 1-9')
#             else:
#                 break
            
#         except ValueError as val_err:
#             print('Error: You entered a number that is not recognized, please enter another.')
#     return play
       


# main()
import random
oa = random.randint(0,100)
a = random.randint(0,100)
#mimicks score
i = 10
again = 'y'
#enter the loop
while again == 'y':
    #first random
    print(f'c={oa}')
    #player guesses
    b = input('guess if h or l')
    #second random to become old random
    print(f'c={a}')
    #condition
    if b == 'h' and a>oa:
        i+=1
        oa =a
        a = random.randint(0,100)
    else:
        i-=1
        oa = a
        a = random.randint(0,100)
        #score assertion
    print(i)
    #loop again?
    again= input('again?')
