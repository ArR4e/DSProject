from turtle import *
from random import randint

def hulknurk(külgede_arv, küljepikkus):
    x = külgede_arv
    while 0 < külgede_arv:
        forward(küljepikkus)
        right(360 / x)
        külgede_arv -= 1

#lisasin forwardile ja random numbritele piirangud, 
#et turtle enamvähem piirides püsiks

#ning ma printisin endale külgede arvu ja küljepikkust,
#sest seda oli huvitav teada

i = 1
while i <= 30:
    up()
    right(randint(0, 360))
    forward(randint(1, 200))
    down()
    
    külgede_arv = randint(3, 50)
    print("Külgede arv:" + str(külgede_arv))
    küljepikkus = randint(1, 100)
    print("Küljepikkus:" + str(küljepikkus))
    
    hulknurk(külgede_arv, küljepikkus)
    
    i += 1
    


