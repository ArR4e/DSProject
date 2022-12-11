from turtle import*
def fraktal(sügavus, pikkus):
    if sügavus < 1:
        return
    else:
        for i in range(4):
            forward(pikkus)
            left(90)
            if < 3:
                fraktal(sügavus - 1, pikkus // 2)
            left(180)
                
fraktal(2, 100)

    