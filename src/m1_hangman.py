"""
Hangman.

Authors: Carter Myers and Michael Johnson.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######
import random

def main():
    word = given_word()
    dashes = len(word)
    guesses = difficulty()
    s = []
    for k in range(dashes):
        s = s + ['_ ']
    while True:
        if guesses == 0:
            print('You Lose!')
            print('Word was: ', word)
            break
        for k in range(len(s)):
            print(s[k], end='')
        print()
        print('Guesses Left: ', guesses)
        num = 0
        letter = user_guess()
        for j in range(len(word)):
            if letter == word[j]:
                s[j] = letter
                num = num + 1
            else:
                num = num
        if num == 0:
            print('Try Again!')
            guesses = guesses - 1
        else:
            print('Good Guess!')
        if won(word, s) == True:
            print('Congratulations! You Won!')
            break
    Q = int(input('Hit 1 if you would like to play again.'))
    if Q == 1:
        main()
    else:
        print('GoodBye!')


def random_word():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
        sequence = []
        sequence = words
        r = random.randrange(0, len(sequence) - 1)
        item = sequence[r]
        return item

def min_length():
    string = input('Choose a minimum word length, por favor:')
    integer = int(string)
    return integer

def given_word():
    num = min_length()
    while True:
        word = random_word()
        if num <= len(word):
            return word

def user_guess():
    string = input('Guess a letter my dude:')
    letter = str(string)
    return letter

def right_letter(word):
    dashes = len(word)
    for k in range(dashes):
        print('_ ', end='')
    print()
    while True:
            num = 0
            letter = user_guess()
            for k in range(len(word)):
                if letter == word[k]:
                    num = num + 1
                    print('Good Guess! UwU')
                    return word
                else:
                    num = num + 0
            if num == 0:
                print('Choose again OwO')

def rights_wrongs_dashes():
    secret = []
    while True:
        dashes = len(right_letter(given_word()))
        for j in range(dashes):
            secret = secret + ['_ ']
        for k in range(dashes):
            print('_ ', end='')
        print()

def won(word, seq):
    num = 0
    for k in range(len(word)):
        if word[k] == seq[k]:
            num = num + 1
        else:
            num = num
    if num == len(word):
        return True
    else:
        return False

def difficulty():
    diff = int(input('How many lives do you want?'))
    return diff














main()

