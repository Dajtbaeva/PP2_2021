from random import randint
a, g = randint(1, 20), 0

name = input('Hello! What is your name?\n')
print(f'\nWell, {name} I am thinking of a number between 1 and 20.')

while True:
    n = int(input('Take a guess.\n'))
    if n > a:
        g += 1
        print('\nYour guess is too high.')
    elif n < a:
        g += 1
        print('\nYour guess is too low.')
    elif n == a:
        print(f'\nGood job, {name}! You guessed my number in {g} guesses!')
        break