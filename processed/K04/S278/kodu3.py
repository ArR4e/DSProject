import turtle
def hulknurk(külgedeArv, küljepikkus):
    for i in range(külgedeArv):
        turtle.forward(küljepikkus)
        turtle.left(360/külgedeArv)
külgedeArv = int(input("Sisestage külgede arv: "))
küljepikkus = int(input("Sisestage küljepikkus: "))
hulknurk(külgedeArv, küljepikkus)