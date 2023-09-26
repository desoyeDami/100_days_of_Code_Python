from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

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

        self.segments[0].fd(MOVE_DISTANCE)