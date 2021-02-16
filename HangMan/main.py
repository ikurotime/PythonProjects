# Step 4

import random
import hangman_words
import hangman_art

end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
print(hangman_art.logo)
lives = 6
# Testing code
#print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    print(f'Lives : {lives}')
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

        # TODO-2: - If guess is not a letter in the chosen_word,
        # Then reduce 'lives' by 1.
    if guess not in chosen_word:
        lives -= 1
        # If lives goes down to 0 then the game should stop and it should print "You lose."
        if lives == 0:
          end_of_game = True
          print('You lose.')
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has
    #  remaining.
    print(f'Lives : {lives}')
    print(hangman_art.stages[lives])
