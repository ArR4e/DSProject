from turtle import *
import random

def kilpkonn(arv, pikkus):
    for i in range(arv):
        forward(pikkus)
        right(360 / arv)
      
print(kilpkonn(random.randint(3, 10), random.randint(10, 100)))

i = 1

while i < 30:

    up()
    setposition(random.randrange(500), random.randrange(500))
    down()
    
    print(kilpkonn(random.randint(3, 10), random.randint(10, 100)))
    
    i += 1
    
    
