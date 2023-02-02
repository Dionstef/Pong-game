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

# Set buttons for movement of puddles
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
    left_paddle.bound_puddle()
    right_paddle.bound_puddle()

    # Ball moving
    ball.move()

    # Ball interaction with wall. Avoid checking again while the ball leaves.
    if (ball.ycor() >= SCREEN_HEIGHT / 2 - 20 and 0 <= ball.heading() <= 180) \
            or (ball.ycor() <= -SCREEN_HEIGHT / 2 + 20 and 180 <= ball.heading() <= 360):
        ball.change_direction("y")

    # Ball interaction with paddles. Avoid checking again while the ball leaves.
    if (right_paddle.distance(ball) < 40 and ball.xcor() > SCREEN_WIDTH / 2 - 60 and (90 >= ball.heading() or ball.heading() >= 270)) \
            or (left_paddle.distance(ball) < 40 and ball.xcor() < -(SCREEN_WIDTH / 2 - 60) and 90 <= ball.heading() <= 270):
        ball.change_direction("x")

    # SCORE
    if ball.xcor() >= SCREEN_WIDTH / 2 - 20 or ball.xcor() <= -(SCREEN_WIDTH / 2 - 20):
        #  Update score for RIGHT player
        if ball.xcor() <= -(SCREEN_WIDTH / 2 - 20):
            score_right.update_score()
            # Check if RIGHT player wins
            if score_right.score >= NUMBER_OF_GOALS:
                score_right.game_over("RIGHT")
                game_is_on = False
        #  Update score for LEFT player
        elif ball.xcor() >= SCREEN_WIDTH / 2 - 20:
            score_left.update_score()
            # Check if LEFT player wins
            if score_left.score >= NUMBER_OF_GOALS:
                score_left.game_over("LEFT")
                game_is_on = False

        # Return ball to initial position and initialize random direction
        ball.init_random_direction()
        screen.update()
        time.sleep(1)  # Pause after each goal

screen.exitonclick()
