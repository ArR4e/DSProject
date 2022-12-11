from turtle import *
speed(0)
def ruut(a,mõõt):
    if a==0:
        return
    else:
        for i in range(4):
            forward(mõõt)
            left(90)
            if i<3:
                ruut(a-1,mõõt/2)
            left(180)
ruut(7,200)
exitonclick()