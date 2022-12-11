from turtle import *
from random import *

#tekitab akna kilpkonnas
screen = Screen()
screen.screensize(500, 500)
screen.setup(500, 500)


#joonistab ühe sisenurga ette antud külgede arvu ja külje pikkuse järgi
def hulknurgad(külgede_arv, külje_pikkus):
    sisenurk = ((külgede_arv - 2) * 180) / külgede_arv
    for i in range(külgede_arv):
        color('navy')
        fd(külje_pikkus)
        lt(180 - sisenurk)
        
        

for i in range(30):
    penup()
    goto(randint(-400, 400), randint(-300, 300))
    pendown()
    hulknurgad(randint(3, 10), randint(10, 200))

turtle.exitonclick()
    