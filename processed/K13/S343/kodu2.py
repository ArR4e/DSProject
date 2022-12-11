import turtle
y=100
def fraktal(sügavus, y):
    if sügavus == 1:
        turtle.forward(y)
        turtle.left(90)
        turtle.forward(y)
        turtle.left(90)
        turtle.forward(y)
        turtle.left(90)
        turtle.forward(y)
    else:
        turtle.forward(y)
        turtle.right(90)
        fraktal(sügavus-1, y*0.5)
        turtle.left(270)
        turtle.forward(y)
        turtle.right(90)
        fraktal(sügavus-1, y*0.5)
        turtle.left(270)
        turtle.forward(y)
        turtle.right(90)
        fraktal(sügavus-1, y*0.5)
        turtle.left(270)
        turtle.forward(y)
fraktal(4, y)
turtle.exitonclick()