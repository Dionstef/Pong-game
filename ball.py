from turtle import Turtle
from random import choice

# Constants
BALL_SPEED = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)  # Make it a bit smaller
        self.move_speed = 0.03  # Initial move speed

    def move(self):
        self.forward(BALL_SPEED)

    # Function for changing direction in given axis
    def change_direction(self, axis):
        old_heading = self.heading()
        if axis == "y":
            self.setheading(-old_heading)  # Reverse direction
        else:
            self.setheading(180 - old_heading)

        self.tilt(old_heading - self.heading()) # Tilt to remain square
        self.move_speed *= 0.9  # Increase move speed everytime the balls bounces

    # Function for initializing ball to a random direction.
    # Not too steep (90 deg or 270 deg) or straight to the players (0 deg or 180 deg)
    def init_random_direction(self):
        self.home()
        self.settiltangle(0)
        init_direction = choice([i for i in range(20, 340) if
                                 i not in range(70, 110) and i not in range(250, 300) and i not in range(160, 200)])
        self.setheading(init_direction)
        self.tilt(-self.heading())  # Tilt to remain square
        self.move_speed = 0.03  # Reset move speed
