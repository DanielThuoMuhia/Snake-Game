from turtle import Turtle, Screen

# Constants for snake's starting positions and movement directions
STARTING_POSITION  = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions of the snake segments
MOVE_DISTANCE = 20  # Distance the snake moves with each step
UP = 90  # Upward direction (90 degrees)
DOWN = 270  # Downward direction (270 degrees)
LEFT = 180  # Leftward direction (180 degrees)
RIGHT = 0  # Rightward direction (0 degrees)

class Snake:
    
    def __init__(self):
        """Initialize the snake by creating its segments and setting the head of the snake."""
        self.segments = []  # List to store the segments of the snake
        self.create_snake()  # Create the initial snake
        self.head = self.segments[0]  # The head of the snake is the first segment

    def create_snake(self):
        """Create the initial snake with three segments at the starting positions."""
        for position in STARTING_POSITION:
            self.add_segment(position)  # Add each segment to the snake

    def add_segment(self, position):
        """Add a new segment to the snake at a given position."""
        new_segment = Turtle("square")  # Create a new turtle segment in the shape of a square
        new_segment.color("white")  # Set the color of the segment to white
        new_segment.penup()  # Lift the pen to avoid drawing lines
        new_segment.goto(position)  # Move the segment to the specified position
        self.segments.append(new_segment)  # Add the segment to the list of segments

    def extend(self):
        """Extend the snake by adding a new segment at the end."""
        self.add_segment(self.segments[-1].position())  # Add a new segment at the position of the last segment

    def move(self):
        """Move the snake forward by moving each segment to the position of the previous segment."""
        # Move each segment to the position of the segment in front of it, starting from the tail
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # Get the x-coordinate of the segment in front
            new_y = self.segments[seg_num - 1].ycor()  # Get the y-coordinate of the segment in front
            self.segments[seg_num].goto(new_x, new_y)  # Move the current segment to the new position
        self.head.forward(MOVE_DISTANCE)  # Move the head forward by the move distance

    def up(self):
        """Change the snake's direction to up if it is not currently moving down."""
        if self.head.heading() != DOWN:  # Prevent the snake from moving in the opposite direction
            self.head.setheading(UP)  # Set the head's direction to up

    def down(self):
        """Change the snake's direction to down if it is not currently moving up."""
        if self.head.heading() != UP:  # Prevent the snake from moving in the opposite direction
            self.head.setheading(DOWN)  # Set the head's direction to down

    def left(self):
        """Change the snake's direction to left if it is not currently moving right."""
        if self.head.heading() != RIGHT:  # Prevent the snake from moving in the opposite direction
            self.head.setheading(LEFT)  # Set the head's direction to left

    def right(self):
        """Change the snake's direction to right if it is not currently moving left."""
        if self.head.heading() != LEFT:  # Prevent the snake from moving in the opposite direction
            self.head.setheading(RIGHT)  # Set the head's direction to right



        