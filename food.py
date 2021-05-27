from turtle import Turtle
import random


class Food(Turtle):
    """
    A class used to represent a Food item, a white pellet for Snakes to eat.
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # Create a circle of size 10x10.
        # Turtles default to size 20x20, so stretch each dimension by 0.5 multiplier.
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """
        Create and spawn a Food item in a random location.
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
