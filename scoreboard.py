from turtle import Turtle

# Constants
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    A class used to draw the game score.
    """

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)  # Move to top-middle of screen
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Update the scoreboard with the latest score and high score.
        """
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)  # Write at center of screen
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        """
        Reset the scoreboard to a score of 0.
        Before resetting, write the latest high score to "data.txt".
        """
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                # Write the high score to the file as a string.
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """
        Update the score by 1 point.
        """
        self.score += 1
        self.update_scoreboard()