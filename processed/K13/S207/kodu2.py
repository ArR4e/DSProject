from turtle import *

def fraktal(suurus, sügavus):
    global kontrollitud
    if sügavus % 2 != 0 and not kontrollitud:
        seth(270)
    kontrollitud = True
        
    for _ in range(0,3):
        fd(suurus)
        if sügavus > 0:
            fraktal(suurus/2, sügavus - 1)
        if sügavus == 0:
            rt(90)
    fd(suurus)
    
speed(0)
tracer(0, 0)
ht()

up()
setpos(-100,100)
down()

kontrollitud = False
fraktal(300, 9)
update()
exitonclick()

    
    
