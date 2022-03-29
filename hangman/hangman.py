import random
import string

from hangman.hangmanwords import words


def get_valid_word(words):
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left. Letters already used: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1
                print('letter is not in the word.')
        elif user_letter in used_letters:
            print('You have already used this letter, pls try again')
        else:
            print('Invalid character, pls try again')
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You guessed it! The word was ', word, '!')

hangman()
