from art import logo
from art import vs
from game_data import data
from os import system
import random

data_a = []
data_b = []
score = 0
def clear():
    _ = system('clear')
def get_user(data_list: list):
    users = random.choice(data).values()
    for key in users:
        data_list.append(key)

get_user(data_a)
get_user(data_b)

while 1:
    clear()
    data_a = data_b
    data_b = []
    get_user(data_b)
    print(logo)
    print(f"Compare A:{data_a[0]}, a {data_a[2]} from {data_a[3]}")
    print(vs)
    print(f"Against B:{data_b[0]}, a {data_b[2]} from {data_b[3]}")
    if data_a == data_b:
        continue
    if score >= 1:
        print(f"You are right! Current score {score}.")
    user_answer = input("Who has more followers? Type 'A' or 'B': ")
    if data_a[1] > data_b[1]:
        right_answer = 'A'
    elif data_a[1] < data_b[1]:
        right_answer = 'B'
    if user_answer != right_answer:
        break
    else:
        score += 1
print(f"Sorry, that's wrong. Final score {score}")