import turtle
t = turtle.Turtle()

def fraktal(x,n):
    if n == 0:
        return x
    for i in range(4):
        t.forward(x)
        t.left(90)
        if i < 3:
            fraktal(x*0.5,n-1)
        t.left(180)
        
