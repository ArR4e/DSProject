from turtle import *
def kilpkonn(sügavus):
    if sügavus == 0:
        return
    else:
        for i in range(sügavus + 1):      
            forward(100)
            left(90)
            if i < sügavus:
                for i in range(sügavus + 1):
                    forward(100)
                    left(90)
                    if i < sügavus:
                        for i in range(sügavus + 1):
                            forward(100)
                            left(90)
                            forward(100)
                            if i < sügavus:
                                for i in range(sügavus + 1):
                                    right(90)
                                    forward(100)
                                    left(90)
                                    forward(100)
                                    right(90)
                    left(180)
            left(180)
        exitonclick()
        return kilpkonn(sügavus - 1)
       
print(kilpkonn(2))