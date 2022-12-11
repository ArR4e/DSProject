from turtle import*
suund = 90
def ruut(level,pikkus):
    global suund
    for i in range(3):
        forward(pikkus)
        if level > 1:
            pikkus = pikkus / 2
            suund = - suund
            ruut(level-1,pikkus)
            suund = - suund
            pikkus *= 2
        right(suund)
    forward(pikkus)
    right(suund)
speed(0)
ruut(3,100)
    