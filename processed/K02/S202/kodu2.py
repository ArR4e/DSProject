from math import *
lp = int(input("Sisestage liini pikkus: "))
#lp = l(iini)p(ikkus)

pmk = int(input("Sisestage postide maksimum kaugus: "))
#pmk = p(ostide)m(max)k(kaugus)

mpv = ((lp/pmk) + 1)
#mpv = m(itu)p(osti)v(aja)

print("Vaja läheb " + str(ceil(mpv)) + " post(i).")