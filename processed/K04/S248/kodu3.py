from turtle import *
from random import randint

def hulknurk(x,y):
    for i in range (0,x):
        forward(y)
        right(180-((x-2)*180)/x)
        i+=1
        
for i in range (0,30):
    külg=randint(0, 100)
    nurgad=randint(3,10)
    hulknurk(nurgad,külg)
    up()
    left(randint(0, 360))
    forward(randint(0,100))
    down()
    
exitonclick()