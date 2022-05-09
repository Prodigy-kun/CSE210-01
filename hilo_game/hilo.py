import random
# from hilo_game import director
class Hilo:
     # Attributes:
        #     old_random (int): A random card chosen from a group of 13
        #     new_random (int): A random card chosen from a group of 13
        #     init-score (int): score point after a guess.
        # """
    def __init__(self):
        #assigning state varriables that generates a random number from 1-13
        self.old_random = random.randint(1,13)
        self.new_random = random.randint(1,13)
        self.init_score= 0

    def verify(self):
        #a method that displays a random card and request a guess from the user
        print(f'The card is {self.old_random}')
        guess = input('Guess if the next card will be higher or lower[H/L]').lower()
        print(f'The new card is {self.new_random}')
        #verify the guess answer according to some conditions
        if guess== 'h' and self.new_random > self.old_random:
            #add the scores to the initial score as long as the condition is met
            self.init_score += 100
            #make the first random to be displayed next
            self.old_random = self.new_random
            # generates a new random which will be used in the next round
            self.new_random = random.randint(1,13)
        elif guess == 'h' and self.new_random < self.old_random:
            self.init_score -= 75
            self.old_random = self.new_random
            self.new_random = random.randint(1,13)
        elif guess == 'l' and self.new_random < self.old_random:
            self.init_score += 100
            self.old_random = self.new_random
            self.new_random = random.randint(1,13)
        elif guess == 'l' and self.new_random > self.old_random:
            self.init_score -= 75
            self.old_random = self.new_random
            self.new_random = random.randint(1,13)
        else:
            self.init_score += 0
            self.old_random = self.new_random
            self.new_random = random.randint(1,13)
        #return the score after assertion of conditions.
        return self.init_score

        
        