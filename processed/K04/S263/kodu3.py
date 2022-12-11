from turtle import*
import random
from random import randint

k=1
while k<31:
    k+=1
    
    n=random.randint(3,20)
    külg = random.randint(15,50)

    def hulknurk(n, külg):
        i = 0
        nurk = 360 / n
        while (i < n):
            forward(külg)
            left(nurk)
            i=i+1
    #up()
    #forward(random.randint(0,100))
    #down()
    
    up()
    left(randint(0,150))
    forward(randint(0,150))
    down()
    
    hulknurk(n,külg)

exitonclick()