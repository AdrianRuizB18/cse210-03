from jumper.game import word
from jumper.game import jumper  
from jumper.game import player 
from jumper.game import letter


class Main:
    def __init__(self):
        pass

    while True:
        word_bank = word()
        player1 = player()
        game = letter()
        
        word_bank.pick_topic()
        word_bank.pick_word()

        while word_bank.not_solved and player1.lives > 0:
            while player1.guess_validation_incomplete:
                player1.guess()
                game.validate_user_input(player1)
                game.check_answer_update_lives(word_bank,player1)
            print(word_bank.current_word_display)
            player1.guess_validation_incomplete = True
            word_bank.check_solve()

        if not word_bank.not_solved:
            print('\nYou win!')

        else:
            print('\nYou lose')
            print('Word was {}').format(word_bank.current_word)

        replay = input('Press any key to play again, x to quit: ')
        print('\n')
        if replay.upper() == 'X':
            break
