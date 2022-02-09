class letter:
    def __init__(self):
        self._letter = ""


    def validate_letter(self, letter):
        """Validates if the user's input is a valid character, 
        then returns the letter in lowercase if it is. Returns false if it's not
        """
        if letter.isalpha():
            self._letter = letter.lower()
            return self._letter
        else: 
            return False
