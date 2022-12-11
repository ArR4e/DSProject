from turtle import *
def ruudud(küljed, pikkus, tase):
    if tase == 0:
        return
    for i in range(küljed):
        fd(pikkus)
        lt(180-360/küljed)
        
        if i < küljed - 1:
            ruudud(küljed, 0.5*pikkus, tase-1)
            
        lt(180)
speed(0)
hideturtle()
ruudud(4,800,10)
exitonclick()