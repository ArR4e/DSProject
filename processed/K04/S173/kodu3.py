from turtle import*
from random import*

def f(a, b):
    x=a
    while x>0:
        forward(b)
        right(360/a)
        x-=1
speed(0)
z=30
while z>0:
    a = randint(3, 20) #randint(3, 20), sest üle 20 külje muutub asi suht ringiks
    b = randint(5, 100) #randint(5, 100), selleks, et asi üldiselt ekraanil püsiks
    f(a, b)
    penup()
    home()
    right(randint(0, 360))
    forward(randint(1, 300))#0 pole kaasa arvatud, sest esimene hulknurk algab juba alguspunktist(home())
    pendown()
    z-=1
exitonclick()