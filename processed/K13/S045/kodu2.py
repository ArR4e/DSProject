import turtle
        
def joonista_ruut(sügavus, pikkus, suund=90): #default suund
    for i in range(3):
        turtle.forward(pikkus)
        
        if sügavus > 1:
            joonista_ruut(sügavus - 1, pikkus / 2, -suund)
        turtle.right(suund)
    turtle.forward(pikkus)
    turtle.right(suund)
            
turtle.speed("fastest")
turtle.pendown()
joonista_ruut(4, 100)