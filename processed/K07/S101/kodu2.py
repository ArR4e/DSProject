f=open("taksohinnad.txt")
kilomeetrid=float(input("Sisesta teepikkus kilomeetrites:"))
odav=-1
def hind(ss,kmh,km):
    #sisseastumine+kilomeetrihind*teepikkus
    hind=ss+kmh*km
    return hind

for rida in f:
    nimi=""
    sisen=""
    kmhind=""
    i=0
    if rida[i]!="":
        while True:
            if rida[i]==",":
                i+=1
                break
            else:
                nimi+=rida[i]
                i+=1
        while True:
            if rida[i]==",":
                i+=1
                sisen=float(sisen)
                break
            else:
                sisen+=rida[i]
                i+=1
        while True:
            if len(rida)==i:
                kmhind=float(kmhind)
                break
            else:
                kmhind+=rida[i]
                i+=1
    
    uus=hind(sisen,kmhind,kilomeetrid)
    if uus<odav or odav==-1:
        odav=uus
        nodav=nimi
    
try:
    print(odav,nodav)
except:
    print("midagi on valesti")
