from turtle import*
speed(0)
def ruutfraktal(sügavus, mõõt):
    if sügavus>1:
        for i in range(4):
            fd(mõõt)
            left(90)
            if i <3:
                ruutfraktal(sügavus-1, mõõt/2)
                left(180)
        left(180)
    else:
        for i in range(4):
            fd(mõõt/2)
            left(90)
            left(180)
ruutfraktal(4, 100)