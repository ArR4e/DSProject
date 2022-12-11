from turtle import*
from random import randint

def kilpkonn():
    
    küljed=randint(3,8)
    küljepikkus=randint(5,20)

    for i in range(küljed):
        forward(küljepikkus)
        left(360/küljed)
        
    up()
    goto(randint(-100,140),randint(-200,150))
    down()
for i in range(30):
    kilpkonn()
exitonclick()
