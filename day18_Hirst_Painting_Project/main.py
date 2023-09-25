import random
import turtle as t

color_list = [(199, 163, 119), (216, 209, 212), (210, 213, 218), (165, 187, 163), (38, 95, 116), (125, 38, 29), (51, 35, 34), (156, 77, 55), (114, 73, 82), (119, 163, 174), (196, 99, 73), (49, 130, 103), (126, 34, 42), (18, 56, 42), (215, 197, 121), (7, 65, 84), (102, 149, 73), (186, 152, 156), (78, 35, 38), (216, 158, 29), (176, 202, 180), (19, 80, 97), (218, 180, 171), (209, 182, 186), (161, 111, 116), (97, 142, 153), (171, 200, 206), (39, 76, 63)]

tim = t.Turtle()
t.colormode(255)
tim.shape("circle")
tim.ht()

tim.penup()
n = 10
tim.setx((-23 * n))
tim.penup()
tim.sety(230)
tim.speed("fastest")
def create_dots(n):
    """Function that creates 10 dots with random colors."""
    for _ in range(n):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.fd(50)
        tim.pendown()


def move_right():
    """Function that moves pen right."""
    tim.rt(90)
    tim.penup()
    tim.fd(50)
    tim.rt(90)
    tim.fd(50)
    tim.down()

def move_left():
    """function that moves pen left."""
    tim.lt(90)
    tim.penup()
    tim.fd(50)
    tim.lt(90)
    tim.fd(50)
    tim.down()


for _ in range(5):
    create_dots(n)
    move_right()
    create_dots(n)
    move_left()


my_screen = t.Screen()
my_screen.exitonclick()

