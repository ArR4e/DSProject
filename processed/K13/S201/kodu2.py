from turtle import *
def ruut(n):
    global pikkus, suund
    for _ in range(3):
        forward(pikkus)

        if n > 1:
            pikkus /= 2
            suund = - suund
            ruut(n - 1)
            suund = - suund
            pikkus *= 2
        right(suund)
    forward(pikkus)
    right(suund)
    
pikkus = 100
suund = 90
hideturtle()
exitonclick()
