# -*- coding: utf-8 -*-

# Trabalho Prático: Programar o jogo da forca
# Prazo: 7 de jul 23:59

# Luis Marti Orosa
# Programe o jogo da forca (https://pt.wikipedia.org/wiki/Jogo_da_forca)
# a partir do arquivo 'jogodaforca.py' completando as funções
# não implementadas do mesmo.

# Importante:
# * Edite o cabeçalho do arquivo para incluir seu nome e matrícula.
# * Entregue o resultado via google classroom antes da data limite.
# * O código está também disponível em:
# https://github.com/rio-group/Prog1-trabalho

# Os arquivos que você adicionar ou criar poderão ser visualizados
# e editados pelo seu professor

# ******************************************************************

import random
from unicodedata import normalize

WORD_LIST = ("hangman", "chairs", "backpack", "bodywash", "clothing",
             "computer", "python", "program", "glasses", "sweatshirt", "sweatpants",
             "mattress", "friends", "clocks", "éclair", "biology", "algebra", "suitcase",
             "knives", "ninjas", "jalapeño", "shampoo")

MAX_TRIES = 6


def get_word():
    """
    Returns a random word from word_list
    """

    sw_accent = random.choice(WORD_LIST)

    # Letters will always be upper case and won't contain special characters
    sw_accent = sw_accent.upper()
    secret_word = (normalize('NFKD', sw_accent).encode('ASCII', 'ignore').decode('ASCII'))

    return secret_word


def word_guessed(secret_word, user_letters):
    """
    Returns True if the characters present in user_letters are enough to guess secret_word
    Returns False otherwise. Parameters:

        * secret_word: word to be guessed
        * user_letters: list containing user inputted letters so far
    """

    sw = secret_word[:]
    ul = user_letters[:]
    ul_set = set(ul)
    sw_set = set(sw)

    # Checks if secret word's letters set is a subset of the set containing user inputted letters
    if sw_set.issubset(ul_set):
        return True
    else:
        return False


def wrong_tries(secret_word, user_letters):
    """
    Returns the amount of letters in user_letters that don't show in secret_word
    """

    # Keeping the parameters from being changed by reference
    sw2 = secret_word[:]
    ul2 = user_letters[:]
    ul2_set = set(ul2)
    sw2_set = set(sw2)

    # Counter
    k = 0

    for x in ul2_set:
        if x not in sw2_set:
            k += 1

    return k


def show_letters(secret_word, user_letters):
    """
    Show which letters from secret_word were guessed right so far and all letters
    inputted by user. For example, the output for the secret word "potato" and the input
    p, c, t should be like:

    Secret word: P _ T _ T _
    Letters tried so far: P, C, T
    """

    incomplete_word = []
    for y in secret_word:
        if y in user_letters:
            incomplete_word.append(y)
        else:
            incomplete_word.append('_')

    print('Secret word: ')
    print('')

    # Formatting lists for printing in two different ways
    print(' '.join(str(x) for x in incomplete_word))
    print('')
    print('Letters tried so far: ')
    print('')
    print(*user_letters, sep=', ')
    print('')


def letter_input():
    """
    Allows user letter input. Should guarantee that the input isn't invalid
    (numbers, multiple characters, accents and so on)
    """

    # Using try/except
    while True:
        try:
            while True:
                letter = str(input('Enter a letter: '))

                # Dealing with input errors. The letter should be a one character string
                if not letter.isalpha() or len(letter) != 1:
                    print('')
                    print('Invalid character. Try again...')
                    continue
                else:
                    break
            break
        except TypeError or ValueError:
            print('Invalid character. Try again...')

    print('*' * 35)
    print('')

    # Letters will always be upper case
    letter = letter.upper()
    return letter


def hangman():
    """
    Main function
    """

    print('')
    print('Welcome to hangman game! Bem vindo ao jogo da forca!')
    print('')
    print('*' * 35)
    print('')

    while True:
        secret_word = get_word()

        user_letters = []

        while not word_guessed(secret_word, user_letters) and \
            wrong_tries(secret_word, user_letters) < \
                MAX_TRIES:

                    show_letters(secret_word, user_letters)

                    remaining = MAX_TRIES - \
                        wrong_tries(secret_word, user_letters)

                    print('Remaining tries: ', remaining)
                    letter = letter_input()
                    if letter in user_letters:
                        print('Letter already inputted. Proceding...')
                        print('')
                    else:
                        user_letters.append(letter)

        show_letters(secret_word, user_letters)

        if word_guessed(secret_word, user_letters):
            print('Congratulations! You discovered the secret word and still breathes!')
        else:
            print('¯\\_(ツ)_/¯ You lost.')

        print('')

        # Ensuring a proper run with try/except
        while True:
            try:
                cont = input('Enter C to keep playing: ')
                break
            except TypeError or ValueError:
                print('Invalid input!')
                print('')
        if not (cont == 'C' or cont == 'c'):
            break

    print('')
    print('Game over. See you next time!')


logo = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   
"""

print(logo)

# Main function call
hangman()
