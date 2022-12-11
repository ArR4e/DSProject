from turtle import*

def fraktal(sügavus):
    global pikkus, suund
    for i in range(3):
        forward(pikkus)
        if sügavus > 1:
            pikkus /= 2
            suund = - suund
            fraktal(sügavus - 1)
            suund = - suund
            pikkus *= 2
        right(suund)
    forward(pikkus)
    right(suund)
       
pikkus = 100
suund = 90

exitonclick()