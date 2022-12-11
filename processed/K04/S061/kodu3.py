from turtle import *
def hulknurk(kulg_arv, kulg_pikkus):
    joon_kulgi = 0
    while joon_kulgi < kulg_arv:
        forward(kulg_pikkus)
        left(360 / kulg_arv)
        joon_kulgi += 1

kulg_arv = int(input("Sisestage küljede arvu:"))
kulg_pikkus = float(input("Valige küljede pikkust:"))
        
hulknurk(kulg_arv, kulg_pikkus)
        
exitonclick()