from turtle import Turtle  # Import the Turtle class from the turtle module
import random  # Import the random module for generating random positions

class Food(Turtle):

    def __init__(self):
        """Initialize the food object as a subclass of Turtle."""
        super().__init__()  # Call the parent class (Turtle) initializer
        self.shape("circle")  # Set the shape of the food to a circle
        self.penup()  # Lift the pen to avoid drawing lines
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Resize the food to be smaller (10x10 pixels)
        self.color("blue")  # Set the color of the food to blue
        self.speed("fastest")  # Set the speed of animation to the fastest
        self.refresh()  # Call the refresh method to place the food at a random position

    def refresh(self):
        """Move the food to a random position on the screen."""
        random_x = random.randint(-280, 280)  # Generate a random x-coordinate within the screen bounds
        random_y = random.randint(-280, 280)  # Generate a random y-coordinate within the screen bounds
        self.goto(random_x, random_y)  # Move the food to the new random position




