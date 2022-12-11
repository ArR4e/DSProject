from turtle import *
from random import randint

kordi = 0
def hulknurk(a,b):
    joonistatud = 0
    while joonistatud < a:
        forward(b)
        right(((a-2)*180)/a)
        joonistatud += 1

while kordi < 30:
    hulknurk((randint(3,10)),(randint(100,300)))
    up()
    forward(randint(100,300))
    left(randint(0,180))
    forward(randint(100,300))
    down()
    kordi = kordi + 1

exitonclick()

    
    
    
    