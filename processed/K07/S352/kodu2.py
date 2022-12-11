f=open("taksohinnad.txt","r")

odav=""
h=99999999999999999999999999999999999
km=input("Sisesta tee pikkus km: ")
while True:
    a=f.readline()
    if a=="":
        break
    a=a.strip().split(",")
    nimi=a[0]
    istusisse=a[1]
    kmhind=a[2]
    
    hind=float(istusisse)+float(kmhind)*float(km)
    
    if hind<h:
        odav=nimi
        h=hind
f.close()
print("Kõige odavam on "+odav)
        
    
    
    