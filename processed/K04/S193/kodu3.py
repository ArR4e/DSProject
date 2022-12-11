import turtle
import random


def hulknurgad(n,pikkus):
    h = random.randint (1,100)
    summa = (n -2)*180
    if summa %n == 0:
        nurk = summa //n
        for i in range (n):
            turtle.forward(h)
            turtle.left(180-nurk)
            

arv = 0
while arv < 30:
    arv = arv + 1
    print (arv)
    hulknurgad(random.randint(3, 8), random.randint(3, 8))
    turtle.up()
    turtle.goto(random.randint(-100, 150), random.randint(-100, 150))
    turtle.down()

    
    
       
    
