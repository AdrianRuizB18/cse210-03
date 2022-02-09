class Player:

    def __init__(self):
        self._lives = 5
        self.letter_guess = ""

    def guess(self):
        self.letter_guess = input("Please guess a letter: ")
    
    def get_lives(self):
        return self._lives

    def reduce_lives(self):
        self._lives -= 1

    