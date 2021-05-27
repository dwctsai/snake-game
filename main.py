from turtle import Screen
from snake import Snake  # from snake file import Snake class
from food import Food
from scoreboard import Scoreboard
import time

"""
This program runs the Snake Game.

The player controls the Snake object with the Up/Down/Left/Right arrow keys.
The player's objective is to eat the Food items on the game board to increase their score,
without crashing the head of the snake into its own body or to the border walls.

The current high score is saved in "data.txt".
"""


# Setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # turn off tracer

# Create a Snake
snake = Snake()

# Create a Food
food = Food()

# Create a Scoreboard
scoreboard = Scoreboard()

# Listen for keystrokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Game loop
game_is_on = True
while game_is_on:
    screen.update()  # update the screen
    time.sleep(0.1)  # add a delay

    snake.move()

    # Detect collision with food
    # Snake segments are 20x20.  Foods are 10x10.
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        # Collision has occurred between Snake head segment and a food.
        # Move the food to a new location.
        food.refresh()
        # Extend snake length by 1 segment
        snake.extend()
        # Update scoreboard
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    # Skip the head itself
    # snake.segments[1:] returns a slice of the list of segments excluding the head.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


# Close window if mouse click on screen
screen.exitonclick()