# Sarnaste ruutude fraktal

from turtle import *

speed(0)
delay(0)
penup()
goto(-100,0)
pendown()

def palju_ruute(pikkus, n):
    if n == 1:
        for i in range(4):
            forward(pikkus)
            left(90)
    else:
        for i in range(4):
            forward(pikkus)
            left(90)
            if i < 3:
                right(90)
                palju_ruute(pikkus*0.5, n-1)
                right(90)

        
        

palju_ruute(100, 4)
exitonclick()