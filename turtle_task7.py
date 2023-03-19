import turtle
from math import pi, sin, cos

turtle.shape('turtle')

for i in range(300):
    t = i / 20 * pi
    dx = (1 + 5 * t) * cos(t)
    dy = (1 + 5 * t) * sin(t)
    turtle.pendown()
    turtle.goto(dx, dy)
    turtle.up()
 
