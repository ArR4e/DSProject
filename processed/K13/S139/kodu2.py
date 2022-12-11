from turtle import *
def fraktal(depth):
    global length, direction
    if depth < 1:
        return
    else:
        for i in range(3):
            forward(length)
            length /= 2
            direction = -direction
            fraktal(depth - 1)
            direction = -direction
            length *= 2
            right(direction)
        forward(length)
        right(direction)
length = 100
direction = 90
fraktal(1)
hideturtle()
exitonclick()
    
        