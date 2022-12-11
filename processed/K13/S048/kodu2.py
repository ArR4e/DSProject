from turtle import*

def fraktal(tase, pikkus):
    if tase == 0:
        return  #kui tase on 0 ss mine välja sealt ehk ära midagi enam tee
    else :
        for i in range(1):
            forward(pikkus) #see on see algus mis ei lähe fraktali sisse
            left(90)
            fraktal(tase -1, pikkus *0.4) #lähme fraktali sisse
            right(180) #siia läheb see mis ta teeb kui jõuab lõpp punkti
            forward(pikkus)
            left(90)
            fraktal(tase -1, pikkus *0.4)
            right(180)
            forward(pikkus)
            left(90)
            fraktal(tase -1, pikkus *0.4)
            right(180)
            forward(pikkus)
            right(90)
            
            speed(100)
fraktal(4, 100)
