from turtle import *
speed(10)
def fraktal(sügavus,pikkus):
        if sügavus == 0:
            return
        else:
            fd(pikkus)
            left(90)
            fraktal(sügavus-1,pikkus*0.5)
            fd(pikkus)
            left(90)
            fraktal(sügavus-1,pikkus*0.5)
            fd(pikkus)
            
            #backward(pikkus)
               
fraktal(3,100)
exitonclick()
            
        