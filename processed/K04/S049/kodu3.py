a = input("Sisestage külgede arv: ")
b = input("Sisestage küljepikkus: ")
c = 360 / int(a)

from turtle import*

def hulknurk(a, b):
    left(c)
    for x in range (0, a):
        forward(b)
        left(c)
    print()
hulknurk(a, b)

#ma üritasin, aga ma lihtsalt ei saa hakkama mitte ühegagi