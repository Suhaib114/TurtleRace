import time  # Return the time in seconds since the epoch as a floating point number
import turtle  # Turtle graphics
from turtle import Turtle  # Subclass of RawTurtle, has the same interface
from random import randint  # Return random integer in range [a, b], including both end points

# Windows Setup

window = turtle.Screen()  # pop up the screen
window.title("Turtle Race")  # Name of the window
turtle.bgcolor("black")  # background colour
turtle.color("white")  # text colour
turtle.speed(0)
turtle.penup()  # position is going to change
turtle.setpos(-140, 200)
turtle.write("Turtle Race", font=("Arial", 30, "bold"))
turtle.penup()  # Pull the pen up – no drawing when moving.

# finish_line

stamp_size = 20
square_size = 15
finish_line = 200

turtle.color("white")
turtle.shape("square")
turtle.shapesize(square_size / stamp_size)
turtle.penup()  # Pull the pen up – no drawing when moving.

for i in range(10):
    turtle.setpos(finish_line, (150 - (i * square_size * 2)))  # first row of the finish line
    turtle.stamp()
for j in range(10):
    turtle.setpos(finish_line + square_size,
                  ((150 - square_size) - (j * square_size * 2)))  # 2nd row of the finish line
    turtle.stamp()
turtle.hideturtle()  # Make the turtle invisible

# Turtle 1
turtle1 = Turtle()
turtle1.speed(0)
turtle1.color("forestgreen")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250, 100)  # Move turtle to an absolute position.
turtle1.pendown()

# Turtle 2
turtle2 = Turtle()
turtle2.speed(0)
turtle2.color("red")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250, 50)  # Move turtle to an absolute position.
turtle2.pendown()

# Turtle 3
turtle3 = Turtle()
turtle3.speed(0)
turtle3.color("white")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250, 0)  # Move turtle to an absolute position.
turtle3.pendown()

# Turtle 4
turtle4 = Turtle()
turtle4.speed(0)
turtle4.color("yellow")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-250, -50)  # Move turtle to an absolute position.
turtle4.pendown()

time.sleep(1)  # pause the game for 1 sec before starting

# race start
for i in range(145):
    turtle1.forward(randint(1, 5))
    turtle2.forward(randint(1, 5))
    turtle3.forward(randint(1, 5))
    turtle4.forward(randint(1, 5))
w = turtle1.xcor()  # Return the turtle's x coordinate.
x = turtle2.xcor()
y = turtle3.xcor()
z = turtle4.xcor()

if w > x and w > y and w > z:
    turtle1.forward(20)
    turtle1.write("---------->   Winner", align="left", font="Arial")

elif x > w and x > y and x > z:
    turtle2.forward(20)
    turtle2.write("---------->   Winner", align="left", font="Arial")

elif y > w and y > x and y > z:
    turtle3.forward(20)
    turtle3.write("---------->   Winner", align="left", font="Arial")

elif z > w and z > x and z > y:
    turtle4.forward(20)
    turtle4.write("---------->   Winner", align="left", font="Arial")

turtle.exitonclick()
