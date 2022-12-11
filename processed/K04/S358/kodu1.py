#Kodutöö 4-1
import math as m

def koogi_hind(name, size):
    if name != "šokolaadikook" and name != "ploomikook" and name != "Napoleoni kook":
        raise Exception("Sellist kooki ei leidu")
    if name == "šokolaadikook":
        return(round(0.06*(m.pi*(size/2)), 2))
    if name == "ploomikook":
        return(round(0.04*(m.pi*(size/2)), 2))
    if name == "Napoleoni kook":
        return(round(0.1*(m.pi*(size/2)), 2))
    
nimi = input("Sisesta koogi nimi: ")
suurus = float(input("Sisesta koogi suurus: "))
print("Koogi hind on", koogi_hind(nimi, suurus))