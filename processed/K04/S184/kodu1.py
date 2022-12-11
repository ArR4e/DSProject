from math import*
def koogi_hind(n,r):
    if n=="šokolaadikook":
        pindala_1=pi*r**2
        hind_1=round(pindala_1*0.06,2)
        print(str(hind_1)+"eurot")
        
    elif n=="ploomikook":
        pindala_1=pi*r**2
        hind_2=round(pindala_1*0.04,2)
        print(str(hind_2)+"eurot")
        
    elif n=="Napoleoni kook":
        pindala_2=r**2
        hind_3=round(pindala_2*0.1,2)
        print(str(hind_3)+"eurot")
        
    else:
        print("Sellist kooki andmebaasist ei leitud")
        
while True:
    n=input("Sisesta koogi nimi:")
    r=float(input("Sisesta koogi mõõt sentimeetrites:"))
    koogi_hind(n,r)