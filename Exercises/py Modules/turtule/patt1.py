import turtle


patt = turtle.Turtle()
patt1 = turtle.Turtle()

patt.shape("turtle")
patt.pencolor("red")
patt.pensize(1)
patt.speed(10)
patt1.pencolor("blue")
for i in range(100):
    patt.forward(300)
    patt1.forward(50)
    patt.right(123)
    patt1.left(123)

turtle.done()