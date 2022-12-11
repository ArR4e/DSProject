from turtle import*
from random import*

def asukoht(x,y):
    setx(x)
    sety(y)
    

def hulknurk(nurgad, pikkus):
    i=0
    while i < nurgad:
        down()
        forward(pikkus)
        left(360/nurgad)
        up()
        i+=1
i=0        
while i<30:
    hulknurk(randint(3,10),randint(15, 100))
    asukoht(randint(-300, 300), randint(-300, 300))
    i+=1
exitonclick()