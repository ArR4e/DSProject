from turtle import *
import random

speed(8)

def kujund(külgede_arv, küljepikkus):
    if külgede_arv == 3:
        joonistatud_külgi = 0
        while joonistatud_külgi < 3:
            forward(küljepikkus)
            left(120)
            joonistatud_külgi += 1
        
    elif külgede_arv == 4:
        joonistatud_külgi = 0
        while joonistatud_külgi < 4:
            forward(küljepikkus)
            left(90)
            joonistatud_külgi += 1
        
    elif külgede_arv == 5:
        joonistatud_külgi = 0
        while joonistatud_külgi < 5:
            forward(küljepikkus)
            left(72)
            joonistatud_külgi += 1
        
    elif külgede_arv == 6:
        joonistatud_külgi = 0
        while joonistatud_külgi < 6:
            forward(küljepikkus)
            left(60)
            joonistatud_külgi += 1
            
n = 0
while n < 30:
    külgede_arv = random.randint(3, 6)
    küljepikkus = random.randint(10, 70)
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    up()
    goto(x, y)
    down()
    kujund(külgede_arv, küljepikkus)
    n += 1
    
exitonclick()