import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gameImages = [rock,paper,scissors]

userValue = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
pcValue = random.randint(0, 2)
print(gameImages[userValue])

print(f'Computer chose :\n {gameImages[pcValue]}')

if userValue >=3 or userValue <0:
    print("You typed an invalid value! You lose!")
elif userValue == 0 and pcValue == 2 or userValue == 2 and userValue == 3 or pcValue == 1 and userValue == 2 or pcValue == 0 and userValue == 1:
    print("You win!")
elif pcValue == 0 and userValue == 2 or userValue == 2 and pcValue == 3 or userValue == 1 and pcValue == 2 or  userValue == 0 and pcValue == 1:
    print("You lose!")
elif userValue == pcValue:
    print('It\'s a draw.')

