from turtle import*

def fraktal(sügavus, mõõt):
    for i in range(3):
        fd(mõõt)
        
        if sügavus > 1:
            fraktal(sügavus-1, mõõt/2)
        left(90)
    fd(mõõt)
    right(90)

speed(0)
fraktal(2, 100)

hideturtle()
exitonclick()
