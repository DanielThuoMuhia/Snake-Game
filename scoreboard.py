from turtle import Turtle  # Import the Turtle class from the turtle module

# Constants for text alignment and font settings
ALIGNMENT = "center"  # Align text to the center
FONT = ("Courier", 24, "normal")  # Set font to Courier, size 24, and normal style

class ScoreBoard(Turtle):

    def __init__(self):
        """Initialize the scoreboard object as a subclass of Turtle."""
        super().__init__()  # Call the parent class (Turtle) initializer
        self.score = 0  # Initialize the score to 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.high_score = 0
        self.color("white")  # Set the text color to white
        self.penup()  # Lift the pen to avoid drawing lines
        self.goto(0, 270)  # Position the scoreboard at the top center of the screen
        self.hideturtle()  # Hide the turtle icon (arrow) so only the text is visible
        self.update_scoreboard()  # Display the initial score on the screen

    def update_scoreboard(self):
        """Update the scoreboard with the current score."""
        self.clear()
        self.write(f"Score: {self.score} highscore: {self.high_score}", align=ALIGNMENT, font=FONT)  # Display the current score on the screen


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()    




    def game_over(self):
        """Display the 'GAME OVER' message at the center of the screen."""
        self.goto(0, 0)  # Move to the center of the screen
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)  # Display 'GAME OVER' message

    def increase_score(self):
        """Increase the score by 2 and update the scoreboard."""
        self.score += 2  # Increment the score by 2 points
        self.clear()  # Clear the previous score from the screen
        self.update_scoreboard()  # Update the screen with the new score
