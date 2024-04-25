import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess the State")
image = "blank_states_img.gif"
screen.addshape(image)
state_guess = 0


turtle.shape(image)
database = pandas.read_csv("50_states.csv")
states_list = database['state'].to_list()
already_guessed = []
states_left = []

while state_guess != len(states_list):
    answer_state = screen.textinput(title=f"{state_guess}/{len(states_list)} Correct",
                                    prompt="What's another state's name").title()
    turtle.tracer(0)
    if answer_state == "Exit":
        break
    if answer_state in states_list and answer_state not in already_guessed:
        already_guessed.append(answer_state)
        coord = database[database.state == answer_state]
        x_coord = int(coord['x']) - 15
        y_coord = int(coord['y'])
        turtle.goto(x_coord, y_coord)
        turtle.write(f"{answer_state}", font=("Courier", 8, "normal"))
        state_guess += 1

# states to learn.csv
states_left = [state for state in states_list if state not in already_guessed]

if len(states_left) != 0:
    df = {
        "states_left": states_left
    }

    data = pandas.DataFrame(df)
    data.to_csv("state_left")

turtle.mainloop()
