import turtle
from typing import List, Any

import pandas
#Pantalla y pen
screen = turtle.Screen()
state_name = turtle.Turtle()
state_name.penup()
state_name.hideturtle()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)
screen.addshape(image)
#Constantes
FONT = "Arial", 30, "normal"
#Variables
user_score = 0
guessed_states = []

data = pandas.read_csv("50_states.csv")
states_count = len(data)
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"({user_score}/{states_count})Guess the state",
                                    prompt="What's another state's name")
    #Comprueba cada estado en la lista
    for state in data.state:
        if answer_state.title() == "Exit":
            missing_states = [state for state in data.state if state not in guessed_states]
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv.csv")
            exit()
        #Si el estado escrito coincide con alguno de la lista, registra su nombre y coordenadas
        if answer_state.title() == state:
            state_data = data[data["state"] == f"{answer_state.title()}"]
            state_x = int(state_data["x"])
            state_y = int(state_data["y"])
            #Si el estado escrito no esta en la lista despues de registrarlo, lo añade a la lista de estados
            #adivinados y escribe su nombre, de lo contrario, lo ignora
            if answer_state not in guessed_states:
                user_score += 1
                guessed_states.append(answer_state.title())
                state_name.goto(state_x, state_y)
                state_name.write(state_data.state.item())

state_name.goto(0, 0)
state_name.write(arg="You did it!", align="center", font=FONT)
screen.mainloop()
