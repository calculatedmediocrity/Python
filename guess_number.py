import random


def guess_number():
    random_number = random.randint(0, 10)
    guess = input('Guess a number between 1 and 10: ')
    while guess != random_number:
        if guess.isdigit():
            guess = int(guess)
            if random_number > guess:
                guess = input('Too low. Try one more time: ')
            elif random_number < guess:
                guess = input('Too high. Try one more time: ')
            else:
                return f'Congrats!!! It was {random_number}'
        else:
            guess = input('Please enter an integer number: ')


print(guess_number())
