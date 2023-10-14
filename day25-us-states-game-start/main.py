import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        break
    if answer_state:
        find_state = data[data["state"] == answer_state]
        if not find_state.empty:
            guessed_state.append(answer_state)
            x_cor = find_state.x
            y_cor = find_state.y
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(int(x_cor), int(y_cor))
            t.write(answer_state)

missing_states = [state for state in all_states if state not in guessed_state]
df = pandas.DataFrame(missing_states)
df.to_csv("learn.csv")
