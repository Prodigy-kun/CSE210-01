from hilo import Hilo

class Director:
    def __init__(self):
        # Args:
        #     self (Director): an instance of Director.
        # this condition makes the program to enter in the while loop
        self.is_playing='y'
        #the starting score of the player
        self.init_score = 0
 # a method that contains a loop that runs the game
    def display_hilo(self):
        #invoke the instance of the Hilo class
        hilo = Hilo()
        # self.init_score += hilo.init_score
        #program enters the loop
        while self.is_playing.lower() == 'y':
            #while condition is true
            #call the verify method from the Hilo class
            hilo.verify()
            # Append the scores to the initial one
            self.init_score += hilo.init_score
            #print the scores to the user
            print(f'Your score is {self.init_score}')
            #ask if the user would like to continue playing
            self.is_playing = input('Play again?[Y/N]')
        else:
            print('Thanks for playing')