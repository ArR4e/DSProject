from turtle import *
def hulknurk(külgede_arv, küljepikkus):
    i = 0
    while i <= külgede_arv:
        forward(küljepikkus)
        right(180 - (((külgede_arv - 2) * 180) / külgede_arv))
        i += 1