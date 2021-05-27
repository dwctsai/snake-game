from turtle import Turtle


# Constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    A class used to represent the Snake that the player controls.
    """

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # Create a snake body
        # Each segment is a Turtle with the shape of a square and size 20x20.
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def extend(self):
        # Get the position of the last segment.
        # Then add a segment to that position.
        # Remember in Python for a list [1, 2, 3], list[-1] is 3.
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)  # move the segment off-screen
        self.segments.clear()  # clear the list
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        # Move last segment to second-to-last segment, backwards all the way to the head
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # Move the head segment
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # The snake can't be allowed to move backwards from its current heading
        if self.head.heading() != DOWN:
            # Set the head's heading
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
