from math import pi

def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
            return(round(pi*((0.06)**2)*float(mõõt),2))
    elif nimi == "ploomikook":
            return(round(pi*((0.04)**2)*float(mõõt),2))
    elif nimi == "Napoleoni kook":
            return(round(0.10*(float(mõõt)**2),2))
    else:
         raise Exception("Sellist kooki andmebaasist ei leitud.")

while True:
    z=input("Sisesta koogi nimi ja mõõt: ")
    if z == "":
        break
    q=z.split()
    x=q[0].replace(",","")
    y=q[1]
    if x == "šokolaadikook" or x == "ploomikook" or x == "Napoleoni kook":
        print ("Koogi hind on " +str(koogi_hind(x, float(y))) + " eurot.")
        
        
