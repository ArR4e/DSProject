from math import pi
šok=0.06
plm=0.04
nap=0.10


def koogi_hind(ching,bang):
    uganda=0
    if ching =="šokolaadikook":
        uganda=šok*(pi*bang**2)
    elif ching== "ploomikook":
        uganda=plm*(pi*bang**2)
    elif ching=="Napoleoni kook":
        uganda=nap*(bang**2)
    elif ching=="":
        pass
    else:
        print("Sellist kooki andmebaasist ei leitud")
        question()
        return
    return round(uganda,2)



def question():
    
    nimk=input("sisesta koogi nimi")
    if nimk=="":
        pass
    else:
        mtt=float(input("sisesta koogi mõõt (cm)"))
        print(str(koogi_hind(nimk,mtt)))
        question()

question()
