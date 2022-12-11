from turtle import *
def ruut(külgede_arv,küljepikkus):
    joonistatud_kylgi = 0
    while joonistatud_kylgi < külgede_arv:
        forward(küljepikkus)
        left(360 / külgede_arv)
        joonistatud_kylgi += 1

külgede_arv = int(input("Palun sisesta külgede arv: "))
küljepikkus = float(input("Palun sisesta küljepikkust: "))
ruut(külgede_arv,küljepikkus)

exitonclick()
