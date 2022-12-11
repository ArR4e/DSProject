from turtle import*
def fraktal(sügavus, pikkus):
    if sügavus>0:
        for i in range(4):
            fd(pikkus)
            lt(90)
            if i <3:
                fraktal(sügavus-1,pikkus*0.5)
            lt(180)
            