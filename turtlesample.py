import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle named "artist"
artist = turtle.Turtle()
artist.speed(0)  # Set the speed to the maximum
artist.width(2)

# Define a list of colors
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white"]

# Draw a colorful spiral
for i in range(360):
    artist.pencolor(random.choice(colors))  # Randomly choose a color
    artist.forward(i)
    artist.left(59)  # Angle can be changed to create different patterns

# Hide the turtle and display the window
artist.hideturtle()
turtle.done()
