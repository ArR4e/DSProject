from turtle import *
def f(sügavus, pikkus):
    if sügavus == 0:
        return
    else:
        fd(pikkus)
        f(sügavus - 1, pikkus * 0.5)
        if sügavus % 2 >= 1:
            lt(90)
            fd(pikkus)
            lt(90)
            fd(pikkus)
            lt(90)
            fd(pikkus)
        
def f1(sügavus, pikkus):
    for i in range(3):
        f(sügavus, pikkus)
    fd(pikkus)
    
f1(1, 50)

#kui 2 panna, siis töötab. Muidu mitte.