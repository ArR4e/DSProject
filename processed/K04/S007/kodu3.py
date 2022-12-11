from turtle import *
from random import randint

# külgede_arv= float(input("Sisestage külgedearv: "))
# küljepikkus= float(input("sisestage küljepikkus: "))
speed(1000000)


def f(külgede_arv, küljepikkus):
    nurk = 360/külgede_arv
    while külgede_arv > 0:
        forward(küljepikkus)
        left(nurk)
        külgede_arv -=1
    
        
i=0      
while i <30:
    f(randint(3,15), randint(1,100))
    up()
    setpos(randint(-100,200),randint(-100,200))
    down()
    i+=1
    
exitonclick()

