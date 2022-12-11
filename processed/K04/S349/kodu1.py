from math import pi
 

def koogi_hind(nimi, mõõt):
    if nimi == a_nimi:
        return a * ((mõõt / 2) ** 2 * pi)
    elif nimi == b_nimi:
        return b * ((mõõt / 2) ** 2 * pi)
    elif nimi == c_nimi:
        return c * (mõõt **2)
    elif nimi != a_nimi or nimi != b_nimi or nimi != c_nimi:
        raise Exception ("Sellist kooki andmebaasist ei leitud.")
        
    
a = 0.05
b = 0.04
c = 0.08

a_nimi = "šokolaadikook"
b_nimi = "maasikakook"
c_nimi = "napoleoni kook"

nimi = input("Kirjuta nimisõnana, mis kooki sa soovid tellida: ").lower()    
mõõt = float(input("Kui suur peab olema selle koogi läbimõõt: "))


print("Sinu koogitellimuse hind on", str(round(koogi_hind(nimi,mõõt),2)), "eurot.") 