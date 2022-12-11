import turtle
import random

turtle.speed(10)
turtle.delay(0)

#hulknurga joonistamise meetod
def hulknurk(sidecount, sidelength):
    nurgakraad = 360 / sidecount
    for i in range(sidecount):
        turtle.forward(sidelength)
        turtle.right(nurgakraad)

#joonistame 30 hulknurka
for n in range(0, 31):

    #joonistame suvalise hulknurga mõistuse piirides vahemikkudega
    hulknurk(random.randrange(3, 12), random.randrange(10, 50))

    #liigutame osutit, et hulknurgad kõik ühes koos poleks
    turtle.up()
    #suuname osuti mujale suvalises suunas
    turtle.right(random.randrange(1, 360))
    #liigutame osutit eemale just joonistatud hulknurgast mingi distantsi
    turtle.forward(random.randint(75, 100))
    turtle.down()

turtle.exitonclick()