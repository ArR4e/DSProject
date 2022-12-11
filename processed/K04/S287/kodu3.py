import turtle
import random

#kylg = 
#pikkus = 

def kilpkonn(kylg, pikkus):
        for x in range(kylg):
            turtle.forward(pikkus)
            turtle.left(180 - ((kylg - 2) * 180) / kylg)

for i in range(30):
    kilpkonn(random.randint(3, 20), random.randint(10, 30))
    turtle.penup()
    turtle.right(random.randint(10,180))
    turtle.forward(random.randint(10,40))
    turtle.left(random.randint(10,180))
    turtle.forward(random.randint(1,40))
    turtle.pendown()

    
    

exit()