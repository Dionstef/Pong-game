from turtle import Turtle, Screen

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUMBER_OF_DASHES = 50


# Function for initializing screen
def initialize_screen():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.listen()
    screen.title("Pong game")
    screen.tracer(0)  # Turns off tracer
    return screen


# Function for creating dashed line
def create_dashed_line():
    line = Turtle()
    line.hideturtle()
    line.speed("fastest")
    line.color("white")
    line.width(5)
    line.penup()
    line.goto(0, SCREEN_HEIGHT / 2)  # Go to upper part of screen
    line.setheading(270)  # Heading towards bottom

    # Create dashes
    dist = 0
    while dist <= SCREEN_HEIGHT:
        if line.isdown():
            line.penup()
        else:
            line.pendown()
        line.forward(SCREEN_HEIGHT / NUMBER_OF_DASHES)
        dist += SCREEN_HEIGHT / NUMBER_OF_DASHES
