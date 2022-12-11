a=0
b=True
c=0
listk=["šokolaadikook","ploomikook","Napoleoni kook"]
while b:
    while a<1:
        kok=str(input("Sisestage enda soovitud kook:"))
        if kok in listk:
            a=1
        elif kok =="":
            c=1
            break
            
        else:
            print("Sellist kooki andmebaasist ei leitud")
        
    
    
        
    a=0
    if c ==1:
        break
    surus=float(input("Sisestage suurus:"))
    def koogi_hind(kook,suurus):
        if kook == "šokolaadikook":
            hind=0.06*suurus*suurus*3.1416
        if kook=="ploomikook":
            hind=0.04*suurus*suurus*3.1416
        if kook=="Napoleoni kook":
            hind=0.1*suurus*suurus
        hind=round(hind,2)
        return(hind)
    print(koogi_hind(kok,surus))