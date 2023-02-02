from turtle import Turtle

# Constants
FONT_STYLE = ('Courier', 20, 'normal')


class Score(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(x_position, 260)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.write(f"{self.score}", align='center', font=FONT_STYLE)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def game_over(self, player_name):
        self.home()
        self.write(f"{player_name} PLAYER WINS", align='center', font=FONT_STYLE)
