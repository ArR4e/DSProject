from math import pi

def koogi_hind(a,b):
    if a == "šokolaadikook":
        x = 0.06*pi*(b**2)
        x = round(x,2)
        return x
    elif a == "ploomikook":
        x = 0.04*pi*(b**2)
        x = round(x,2)
        return x
    elif a == "Napoleoni kook":
        x = 0.1*(b**2)
        x = round(x,2)
        return x
    else:
        return "Sellist kooki andmebaasist ei leitud"



m=1
while True:
    m = input("Sisesta koogi nimi: ")
    if m == "":
        break
    n = float(input("Sisesta koogi mõõt: "))
    print(koogi_hind(m,n))


