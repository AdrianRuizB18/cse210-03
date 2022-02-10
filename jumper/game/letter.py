class Letter:
    def __init__(self):
        self._letter = ""
        self.correct = False

    def validate_letter(self, letter):
        """Validates if the user's input is a valid character, 
        then returns the letter in lowercase if it is. Returns false if it's not
        """
        if letter.isalpha() and letter.len() == 1:
            self.correct = True
        else:
            self.correct = False

    def set_letter(self, letter):
        self._letter = letter.lower()
    
    def get_letter(self):
        return self._letter

