from turtle import forward, left, right

def fraktal(sügavus):
    if sügavus == 1:
        left(90)
    else:
        fraktal(sügavus - 1)
        for i in range(4):
            forward(100 / sügavus)
            left(90)
            if i < 3:
                for i in range(4):
                    forward(50)
                    left(90)
                    if i < 3:
                        for i in range(4):
                            forward(25)
                            left(90)
                            left(180)
                    left(180)
            left(180)

