from turtle import*

def fraktal(i):
    i = 4
    if i > 3:
        forward(100)
        left(90)
        fraktal(i-1)
        i = a
        forward(50)
        left(90)
        fraktal(i-1)
        i = a
        forward(25)
        left(90)
        fraktal(i-1)
fraktal(4)
exitonclick()
        
    