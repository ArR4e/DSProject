from math import *
def koogi_hind(n, m):
    if n == ("šokolaadikook"):
        return round(0.06 * (m ** 2 * pi), 2) #šokolaadikook
        
    elif n == ("ploomikook"):
        return round(0.04 * (m ** 2 * pi), 2) #ploomikook
        
    elif n == ("Napoleoni kook"):
        return round(0.1 * (m ** 2), 2) #Napoleoni kook"
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")


while True:
    n = input("Koogi nimi? ")
    if n == (""):
        break
    m = float(input("Mõõt? "))
    print (koogi_hind(n, m))