from math import *
šokolaadikook=0.06
ploomikook=0.04
Napoleoni_kook=0.1
a=True
while a==True:
    def koogi_hind(sort, mõõtmed):
        if sort==str("Napoleoni kook"):
            mõõtmed=mõõtmed**2
            hind=round(0.1*float(mõõtmed),2)
            print("teie tellitud "+ str(sort) + " maksab mõõtmetes " + str(mõõtmed)+ " ruutsentimeetrit " + str(hind) + " eurot.")
        elif sort==str("ploomikook"):
            mõõtmed=mõõtmed**2*pi
            hind=round(0.04*float(mõõtmed),2)
            print("teie tellitud "+ str(sort) + " maksab mõõtmetes " + str(mõõtmed)+ " ruutsentimeetrit " + str(hind) + " eurot.")
        elif sort==str("šokolaadikook"):
            mõõtmed=mõõtmed**2*pi
            hind=round(0.06*float(mõõtmed),2)
            print("teie tellitud "+ str(sort) + " maksab mõõtmetes " + str(mõõtmed)+ " ruutsentimeetrit " + str(hind) + " eurot.")
        elif sort==str(""):
            a==False
        else:
            print("Sellist kooki andmebaasist ei leitud")
koogi_hind(str(input("palus sisestage teie tellitava koogi nimi: ")),float(input("palus sisestage teie tellitava koogi mõõtmed: ")))