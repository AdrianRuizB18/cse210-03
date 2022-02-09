from random import choice

class word:

 
    colors = ['red','blue','green','yellow','pink','orange','black']
    animals = ['dog','cat','bird','horse','snail','monkey','lizard','butterfly']
    topic_names = ['Colors','Animals']
    topics = {'Colors':colors,'Animals':animals}

    def __init__(self):
        self.current_topic = ''
        self.current_word = ''
        self.current_word_display = []
        self.letters_guessed_counter = 0
        self.not_solved = True
        self.letters_already_guessed = []
        
    def pick_topic(self):
        self.current_topic = choice(self.topic_names)
        print('Topic: {}'.format(self.current_topic))

    def pick_word(self):
        self._current_word = choice(self.topics[self.current_topic])
        for i in self.current_word:
            self.current_word_display.append('_')
        print(('Word is {} letters long.').format(len(self.current_word)))
        print(self.current_word_display)

    def check_solve(self):
        self.not_solved = self.letters_guessed_counter < len(self.current_word)
        

