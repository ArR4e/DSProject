from turtle import*
def fraktal(sügavus, küljepikkus):
    if sügavus == 0:
        return
    else:
        for i in range(4):
            forward(küljepikkus)
            left(90)
            if i < 3:
                fraktal(sügavus - 1 , küljepikkus/3)
                if i < 3:
                    fraktal(sügavus -1 , küljepikkus/3)
                left(180)
        left(180)

fraktal(3, 100)     
    