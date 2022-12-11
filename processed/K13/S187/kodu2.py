from turtle import *


def fraktal(aste, kylg):
    Turtle()

    if aste == 0:
        return None

    else:
        forward(kylg)
        right(90)
        forward(kylg)
        right(90)
        forward(kylg)
        right(90)
        forward(kylg)
        right(90)
        forward(kylg)
        right(90)
        forward(kylg)
        left(90)

        fraktal(aste - 1, kylg/2)

# sain ühe nurgaga tööle, kolme nurgaga ei suutnud välja nuputada, ka murelahendaja abiga mitte
# funktsioon fraktal töötab ühe nurgaga, fraktal1 on minu katse kolme nurgaga töötavat funktsiooni luua

'''
def fraktal1(aste, kylg):
    Turtle()
    
    forward(kylg)
    right(90)
    forward(kylg)
    right(90)
    forward(kylg)
    right(90)
    forward(kylg)

    if aste == 1:
        return None
    
    else:
        right(90)
        forward(kylg)
        left(90)
        fraktal(aste - 1, kylg/2)
        left(90)
        fraktal(aste - 1, kylg/2)
        left(90)
        fraktal(aste - 1, kylg/2)

fraktal1(3, 100)
'''