import turtle

ttl = turtle.Turtle()
ttl.pencolor("red")
for i in range(50):
    ttl.forward(i*5) #Moves forward with given value
    ttl.right(144) #Angle clockwise 

turtle.done()