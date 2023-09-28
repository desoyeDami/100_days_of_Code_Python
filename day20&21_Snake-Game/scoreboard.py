from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
