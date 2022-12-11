import turtle
def ruut(sügavus, mõõt):
    if sügavus == 1:
        turtle.forward(mõõt)
        turtle.right(90)
        turtle.forward(mõõt)
        turtle.right(90)
        turtle.forward(mõõt)
        turtle.right(90)
        turtle.forward(mõõt)
    else:
        turtle.forward(mõõt)
        turtle.left(90)
        ruut(sügavus - 1, mõõt * 0.5)
        turtle.left(90)
        turtle.forward(mõõt)
        turtle.left(90)
        ruut(sügavus - 1, mõõt * 0.5)
        turtle.left(90)
        turtle.forward(mõõt)
        turtle.left(90)
        ruut(sügavus - 1, mõõt * 0.5)
        turtle.left(90)
        turtle.forward(mõõt)