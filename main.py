from screen import *
from paddle import Paddle
from ball import Ball
from score import Score
import time

# Constants
NUMBER_OF_GOALS = 10

# Initialize screen
screen = initialize_screen()
create_dashed_line()

# Create paddles at positions
right_paddle = Paddle(SCREEN_WIDTH / 2 - 40, 0)
left_paddle = Paddle(-(SCREEN_WIDTH / 2 - 40), 0)

# Set buttons for movement of paddles
# RIGHT player
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
# LEFT player
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

# Initialize ball
ball = Ball()
ball.init_random_direction()

#  Initialize score counters at positions
score_right = Score(30)
score_left = Score(-30)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)  # Adds small delay and controls move speed

    # Avoid paddles leaving the screen
    left_paddle.bound_paddle()
    right_paddle.bound_paddle()

    # Ball moving
    ball.move()

    # Ball interaction with wall
    if ball.hit_wall():
        ball.change_direction("y")

    # Ball interaction with paddles
    if ball.hit_paddle(ball.distance(right_paddle), ball.distance(left_paddle)):
        ball.change_direction("x")

    # Check if a player scored
    if ball.xcor() <= -(SCREEN_WIDTH / 2 - 20):  # Check for RIGHT player
        score_right.update_score()    # Update score for RIGHT player
        # Return ball to initial position and initialize random direction
        ball.init_random_direction()
        screen.update()
        time.sleep(1)  # Pause after each goal

        if score_right.score >= NUMBER_OF_GOALS:  # Check if RIGHT player wins
            score_right.game_over("RIGHT")
            game_is_on = False

    elif ball.xcor() >= SCREEN_WIDTH / 2 - 20:  # Check for LEFT player
        score_left.update_score()
        # Return ball to initial position and initialize random direction
        ball.init_random_direction()
        screen.update()
        time.sleep(1)  # Pause after each goal

        if score_left.score >= NUMBER_OF_GOALS:  # Check if LEFT player wins
            score_left.game_over("LEFT")
            game_is_on = False


screen.exitonclick()
