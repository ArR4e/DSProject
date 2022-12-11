from turtle import *
speed(0)

def squares(x, le, di):
    for _ in range(3):
        forward(le)
        if x > 1:
            squares(x-1, le/2, -di)
        right(di)
    forward(le)
    right(di)

squares(4, 100, 90)
hideturtle()
exitonclick()

# https://stackoverflow.com/questions/59009062/generating-square-fractals-with-python