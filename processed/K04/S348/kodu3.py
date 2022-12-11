from turtle import *

def hulknurk(külgede_arv, küljepikkus):
    if külgede_arv >= 3:
        for i in range(külgede_arv):
            forward(küljepikkus)
            left(360/külgede_arv)
    else:
        print("Vigane sisend")

