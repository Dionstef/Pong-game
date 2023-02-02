from turtle import Turtle
from screen import SCREEN_HEIGHT

# Constant of moving increments of paddles
MOVE_INCREMENTS = 40


class Paddle(Turtle):
    def __init__(self, init_x, init_y):
        super().__init__()
        self.penup()
        self.goto(init_x, init_y)
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.shapesize(3, 0.8, 1)  # Puddle is 60x16 pixels
        self.speed("fastest")

    # Function for moving up
    def move_up(self):
        current_x, current_y = self.position()
        self.setpos(current_x, current_y + MOVE_INCREMENTS)  # Move by increments of MOVE_INCREMENTS

    # Function for moving down
    def move_down(self):
        current_x, current_y = self.position()
        self.setpos(current_x, current_y - MOVE_INCREMENTS)  # Move by increments of MOVE_INCREMENTS

    # Function for restricting puddle within the screen
    def bound_puddle(self):
        if self.ycor() >= SCREEN_HEIGHT / 2 - 40:  # Upper boundary
            self.sety(SCREEN_HEIGHT / 2 - 40)
        if self.ycor() <= -SCREEN_HEIGHT / 2 + 40:  # Lower boundary
            self.sety(-SCREEN_HEIGHT / 2 + 40)
