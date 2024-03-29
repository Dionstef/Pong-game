from turtle import Turtle
from random import choice
from screen import SCREEN_HEIGHT, SCREEN_WIDTH
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
            self.setheading(-old_heading)  # Reverse direction when hitting a wall
        else:
            self.setheading(180 - old_heading)  # Reverse direction when hitting a paddle
            self.move_speed *= 0.9  # Increase move speed everytime the balls hits a paddle

        self.tilt(old_heading - self.heading())  # Tilt to remain square

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

    # Function for checking if the ball hit the wall
    # Avoids checking again while the ball returns
    def hit_wall(self):
        if (self.ycor() >= SCREEN_HEIGHT / 2 - 20 and 0 <= self.heading() <= 180) \
                or (self.ycor() <= -SCREEN_HEIGHT / 2 + 20 and 180 <= self.heading() <= 360):
            return True
        else:
            return False

    # Function for checking if the ball hit a paddle
    # Avoids checking again while the ball returns
    def hit_paddle(self, distance_right, distance_left):
        if (distance_right < 40 and self.xcor() > SCREEN_WIDTH / 2 - 60 and (90 >= self.heading() or self.heading() >= 270)) \
                or (distance_left < 40 and self.xcor() < -(SCREEN_WIDTH / 2 - 60) and 90 <= self.heading() <= 270):
            return True
        else:
            return False
