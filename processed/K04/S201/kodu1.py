def koogi_hind():
    a= input("Sisesta koogi nimi: ")
    while a == "":
        pass
    b = float(input("Sisesta koogi mõõtmed: "))
    import math
    if a == " šokolaadikook":
        print( round(math.pi * b * b * 0.06 , 2))
    elif  a == "ploomikook":
        print( round(math.pi * b * b * 0.04 , 2))
    elif  a == "Napoleoni kook":
        print( round(b * b * 0.10,2))
    else:
        print("Sellist kooki andmebaasist ei leitud")
while True:
    koogi_hind()

