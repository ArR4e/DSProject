import random
from turtle import *

def joonista(külgede_arv, küljepikkus):
    x = random.randint(1, 200)
    y = random.randint(1, 200)
    nurk = 180 - (((külgede_arv - 2) * 180) / külgede_arv)
    for i in range (0, külgede_arv):
        down()
        fd(küljepikkus)
        left(nurk)
    up()
    setpos(x, y)
    


for i in range (0, 30):
    külg = random.randint(4, 12)
    pikkus = random.randint(30, 100)
    joonista(külg, pikkus)
    