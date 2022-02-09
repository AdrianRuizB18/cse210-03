class Jumper:
    ​
#Iniciate
    def __init__(self):
        self.__draw()
        self.__Wrong = 0
​
#updates the "Wrong" variable
    def __set_Wrong(Mistake):
        self.__Wrong = Wrong
​
#Draw the parachute depending on how many wrong answer the user has given
    def __draw(Wrong):
​
        if Wrong == 1:
            print()
            print(' ____ ')
            print('/____\ ')
            print('\    / ')
            print(' \  / ')
            print('   O  ')
            print('  /|\ ')
            print('  / \ ')
            print()
            print('^^^^^^^')
​
        elif Wrong == 2:
            print()
            print('/____\ ')
            print('\    / ')
            print(' \  / ')
            print('   O  ')
            print('  /|\ ')
            print('  / \ ')
            print()
            print('^^^^^^^')
​
        elif Wrong == 3:
            print()
            print('\    / ')
            print(' \  / ')
            print('   O  ')
            print('  /|\ ')
            print('  / \ ')
            print()
            print('^^^^^^^')
​
        elif Wrong == 4:
            print()
            print(' \  / ')
            print('   O  ')
            print('  /|\ ')
            print('  / \ ')
            print()
            print('^^^^^^^')
​
        elif Wrong == 5:
            print()
            print('   X  ')
            print('  /|\ ')
            print('  / \ ')
            print()
            print('^^^^^^^')