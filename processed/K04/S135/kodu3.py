from turtle import *
from random import randint

# funktsioon, mis joonistab hulknurga turtle mooduliga
def hulknurk(kylgedeArv, kyljepikkus):
    i = kylgedeArv
    while i > 0:
        forward(kyljepikkus)
        left(360 / kylgedeArv)
        i -= 1

i = 30
speed("fastest")

# joonistab 30 hulknurka
while True:
    if i == 0:
        break
    
    pendown()
    hulknurk(randint(3, 9), randint(10, 40))
    left(randint(0, 360))
    penup()
    forward(randint(100, 200))
    
    i -= 1
    
exitonclick()