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
        validation = letter()
        
        word_bank.pick_topic()
        word_bank.pick_word()

        lives = player1.get_lives()
        

        while word_bank.not_solved and lives > 0:
                player1.guess()
                validation.validate_letter(player1.letter_guess)
                while validation.correct == False:
                    if validation.correct == True:
                        validation.set_letter(player1.letter_guess)
                        player1.letter_guess = validation.get_letter()
                        break
                    else:
                        print("Error: Not a letter.")
                        player1.guess()
                        validation.validate_letter(player1.letter_guess)

                    

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
