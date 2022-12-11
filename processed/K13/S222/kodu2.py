from turtle import *

def ruut(a,b,c=90):
    for _ in range(0,3):
        fd(a)
        if b > 1:
            ruut(a/2,b-1,-c)
        rt(c)
    fd(a)
    rt(c)

speed("fastest")
ruut(50,4)
exitonclick()