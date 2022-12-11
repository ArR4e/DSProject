from math import pi

def šok_maksumus(raadius):
    pindala1 = pi * raadius**2
    return round(pindala1 * 0.06, 2)

def ploom_maksumus(raadius):
    pindala2 = pi * raadius**2
    return round(pindala2 * 0.04, 2)

def Napol_maksumus(külg):
    pindala3 = külg * külg
    return round(pindala3 * 0.1, 2)

while True:
    kook = input("Sisesta koogi nimi: ")
    if kook == "":
        break
    else:
        mõõt = float(input("Sisesta koogi mõõt: "))

m1 = šok_maksumus(mõõt)
m2 = ploom_maksumus(mõõt)
m3 = Napol_maksumus(mõõt)

if kook == "šokolaadikook":
    print("Koogi maksumus on " + str(m1))
elif kook == "ploomikook":
    print("Koogi maksumus on " + str(m2))
elif kook == "Napoleoni kook":
    print("Koogi maksumus on " + str(m3))
else:
    print("Sellist kooki andmebaasist ei leitud...")
    
