from math import pi
while True:
    nimi = input("Sisestage koogi nimi: ")
    if nimi == "":
        break
    i=0
    while True:
       try:
           suurus = float(input("Sisestage koogi suurus arvudega: "))
           break
       except:
            print("arvudega siiski (kui kasutate \',\' siis proovige \'.\')")
            i = i+1
       if(i == 10):
            raise Exception("lootusetu olete")
           
    def koogi_hind(nimi, suurus):
        if nimi == "šokolaadikook":
            hind = 0.06*pi*suurus**2
        elif nimi == "ploomikook":
            hind = 0.04*pi*suurus**2
        elif nimi == "Napoleoni kook":
            hind = 0.10*suurus**2
        else:
            raise Exception("Sellist kooki andmebaasist ei leitud")
        return round(hind,2)
    print(koogi_hind(nimi,suurus),"€",sep="")