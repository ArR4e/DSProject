import turtle as t

def ruut(sügavus, pikkus):
    if sügavus >= 1:
        t.forward(pikkus)
        t.left(90)
        ruut(sügavus-1, pikkus/2)
        t.right(180)
        t.forward(pikkus)
        t.left(90)
        ruut(sügavus-1, pikkus/2)
        t.right(180)
        t.forward(pikkus)
        t.left(90)
        ruut(sügavus-1, pikkus/2)
        t.right(180)
        t.forward(pikkus)
        t.right(90)