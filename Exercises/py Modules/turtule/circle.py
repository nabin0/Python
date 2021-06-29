import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)  # set screen colormodde to set rgb color in pencolor
t.pensize(4)  # To set pen size range(1-10)


for i in range(100):
    r = random.randint(1, 120)  # random numbers for red
    g = random.randint(81, 200)  # random numbers for green
    b = random.randint(61, 255)  # random numbers for blue
    t.pencolor(r, g, b)  # set pen color
    t.circle(i*5)
    t.penup()
    t.setposition(0, -i*5)
    t.pendown()

turtle.done()
