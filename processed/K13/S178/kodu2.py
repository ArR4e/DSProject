'''Kirjuta rekursiivne funktsioon, mis joonistab kilpkonnaga fraktali ruudust,
mille kolmes nurgas on sarnased ruudud ning nende kolmes nurgas on ka sarnased ruudud ja
nii edasi vastavalt funktsioonile etteantud sügavusele.

Joonisel on fraktalid, mis tekivad sügavuste 1, 2, 3 ja 4 puhul.'''

from turtle import *

def fraktal(sügavus):
    global pikkus
    global nurk
    for i in range(3):
        forward(pikkus)
            
        if sügavus > 1:
            pikkus /= 2
            nurk = -nurk
            fraktal(sügavus - 1)
            nurk = -nurk
            pikkus *= 2
                
        right(nurk)
        
    forward(pikkus)
    right(nurk)

pikkus = 100
nurk = 90

fraktal(3) 

exitonclick()

'''from turtle import *

def fractal(level):
    global length, direction

    for _ in range(3):
        forward(length)

        if level > 1:
            length /= 2
            direction = - direction
            fractal(level - 1)
            direction = - direction
            length *= 2

        right(direction)

    forward(length)
    right(direction)

length = 100
direction = 90

fractal(3)

hideturtle()
exitonclick()'''