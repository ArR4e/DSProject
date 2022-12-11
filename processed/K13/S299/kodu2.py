import turtle

def frakt(sügavus,pikkus):
    if sügavus==0:
        return
    if sügavus==1:
        for i in range(4):
            turtle.forward(pikkus)
            turtle.left(90)
        turtle.left(180)
    else:
        for i in range(4):
            turtle.forward(pikkus)
            turtle.left(90)
            if i>sügavus:       
                frakt(sügavus-1,pikkus/2)
        turtle.left(180)
        
# ei saa aru, kuidas teha