'''-- Kodutöö nr. 13 - 2. Sarnaste ruutude fraktal --'''
import turtle
########################################################
## funktsioon võtab argumentideks ruudu pikkust ja fraktali sügavust
## ja joonistab 'turtle' abil fraktali kolmes ruudu nurgas
def ruutude_fraktal(pikkus, sügavus):
    
    if sügavus <= 0:
        return
    
    for i in range(3):
        # joonista esimene külg
        turtle.forward(pikkus)
        # pööra vasakule
        turtle.left(90)
        
        # joonista ruut poole küljepikkusega ja sügavus on juba 1 võrra vähem
        ruutude_fraktal(pikkus//2, sügavus - 1)
        
        # pööra vasakule järgmise külje poole ja alusta uuesti (järgmine i)
        turtle.left(180)
    
    # viimane külg ilma fraktaalideta
    turtle.forward(pikkus)
    turtle.left(90)
    turtle.left(180)
    

turtle.speed('fast')
turtle.pensize(2)

ruutude_fraktal(200, 3)

turtle.exitonclick()
turtle.done()