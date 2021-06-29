import turtle

nja = turtle.Turtle()

for i in range(180):
    nja.forward(100)
    nja.right(30)
    nja.forward(20)
    nja.left(60)
    nja.forward(30)
    nja.right(30)

    nja.penup()
    nja.setposition(0,0)
    nja.pendown()

    nja.right(2)

turtle.done()