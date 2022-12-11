from turtle import *
from random import *

def hulknurk(a, b):
    for i in range(a):
        forward(b)
        right(360 / a)

speed(0)

for i in range(30):
    
    penup()
    kylgede_arv = randint(3, 15)
    kyljepikkus = randint(0, 40)
    goto(randint(-200, 200), randint(-200, 200))
    
    pendown()
    hulknurk(kylgede_arv, kyljepikkus)
    
    
done()
