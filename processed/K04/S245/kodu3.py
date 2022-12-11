import turtle

#arvud
pikkus = int(input("Palun sisestage külje pikkus: "))
küljed = int(input("Palun sisestage külgede arv, (soovitavalt 3-10 vahel): "))
nurk = 360/küljed

def hulknurk():
    for i in range(küljed):
        turtle.forward(pikkus)
        turtle.left(nurk)
        
    
hulknurk()
    