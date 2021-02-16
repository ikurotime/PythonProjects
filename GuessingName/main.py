import random

attempts = 5
guess_number = random.randint(1, 100)

print('Welcome to the guess number!')
print('Im thinking in a number from 1 to 100...')
print(f'Psst, the correct answer is {guess_number}!')

difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")

if difficulty == 'easy':
    attempts = 10

print(f'You have {attempts} attempts to guess the number.')


def compare(guess, number):
    if guess > number:
        print('Too high')
    elif guess < number:
        print('Too low')
    if guess == number:
        print(f'You got it! the number was {guess_number}')
        exit()


Guessed = False
while not Guessed:
    user_guess = int(input('Make a guess: '))
    compare(user_guess, guess_number)
    attempts -= 1
    if attempts == 0:
        print("You've run out of guesses, you lose.")
    else:
        print('Guess again')
        print(f'You have {attempts} attempts remaining to guess the number.')
