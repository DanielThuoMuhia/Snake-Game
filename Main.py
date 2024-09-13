from turtle import Screen  # Import the Screen class from the turtle module
from snake import Snake  # Import the Snake class from the snake module
from food import Food  # Import the Food class from the food module
from scoreboard import ScoreBoard  # Import the ScoreBoard class from the scoreboard module
import time  # Import the time module for adding delays

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)  # Set the width and height of the game screen
screen.bgcolor("black")  # Set the background color of the screen to black
screen.title("My Snake Game")  # Set the title of the window
screen.tracer(0)  # Turn off the screen updates to manually control screen refresh

# Create instances of Snake, Food, and ScoreBoard
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Set up key listeners to control the snake
screen.listen()  # Listen for keyboard events
screen.onkey(snake.up, "Up")  # Move snake up when "Up" arrow key is pressed
screen.onkey(snake.down, "Down")  # Move snake down when "Down" arrow key is pressed
screen.onkey(snake.left, "Left")  # Move snake left when "Left" arrow key is pressed
screen.onkey(snake.right, "Right")  # Move snake right when "Right" arrow key is pressed

# Main game loop
game_is_on = True  # Flag to keep the game running
while game_is_on:
    screen.update()  # Refresh the screen to show the latest movements
    time.sleep(0.1)  # Add a delay to control the speed of the snake
    snake.move()  # Move the snake forward

    # Detect collision with food
    if snake.head.distance(food) < 15:  # If the distance between the snake's head and food is less than 15 pixels
        food.refresh()  # Move the food to a new random location
        snake.extend()  # Add a new segment to the snake's body
        scoreboard.increase_score()  # Increase the score

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
       

    # Detect collision with its own tail
    for segment in snake.segments[1:]:  # Iterate through all segments except the head
        if snake.head.distance(segment) < 10:  # If the distance between the head and any segment is less than 10 pixels
            scoreboard.reset()
            snake.reset()
            

        

    
       






screen.exitonclick()