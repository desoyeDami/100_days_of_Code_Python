import random
import turtle as t

is_game_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a colour: ".lower())
colors = ["red", "yellow", "orange", "green", "blue", "purple"]

y_axis = -130
all_turtles = []
for turtle_index in range(6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis)
    new_turtle.color(colors[turtle_index])
    y_axis = y_axis + 50
    all_turtles.append(new_turtle)


if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} is the winner.")
            else:
                print(f"You've lose! The {winning_turtle} is the winner.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
screen.exitonclick()