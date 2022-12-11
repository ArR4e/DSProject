from turtle import *

t = Turtle()
t.speed(0)

def draw_square(a, depth):
    if depth == 0:
        return
    else:
        for i in range(4):
            t.forward(a)
            if i < 3:
                draw_square(a/2, depth-1)
            t.right(90)
        t.left(180)


draw_square(100, 10)
exitonclick()