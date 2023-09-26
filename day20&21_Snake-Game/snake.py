from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x = 0
        for position in range(3):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.goto(x=x, y=0)
            new_segment.color("white")
            self.segments.append(new_segment)
            x -= 20

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            seg_x = self.segments[seg_num - 1].xcor()
            seg_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(seg_x, seg_y)

        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
