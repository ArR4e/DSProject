from turtle import *
from random import randint

suva_külg = randint(3,10)
nurgad = ((suva_külg - 2) * 180) / suva_külg
nurk = 180 - nurgad
pikkus = randint(20,200)

def hulknurk():
    külgede_arv = 0
    
    while külgede_arv < suva_külg:
        forward(pikkus)
        left(nurk)
        külgede_arv += 1
        
def suva_suund():
        up()
        forward(randint(10,200))
        right(randint(10,200))
        down()
        
suva = 0
while suva <30:
    hulknurk()
    suva_suund()
    suva += 1
        
exitonclick()