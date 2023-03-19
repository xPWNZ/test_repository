import turtle

x = 10
while x <= 110:
    turtle.shape('turtle')
    turtle.forward(x*2)
    turtle.left(90)
    turtle.forward(x*2)
    turtle.left(90)
    turtle.forward(x*2)
    turtle.left(90)
    turtle.forward(x*2)
    turtle.penup()
    turtle.goto(-x, -x)
    x += 10
    turtle.left(90)
    turtle.pendown()
