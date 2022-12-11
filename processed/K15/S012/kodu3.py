#kodu 3 - bussid

def h_min(sisend):
    kellaaeg = sisend.split(":")
    minutid = int(kellaaeg[0])*60 + int(kellaaeg[1])
    return minutid

fail = input("Sisesta failinimi: ")
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")
f = open(fail)
sõidud = []
hinnad = []
for rida in f:
    järjend = rida.split(" ")
    väljumisaeg = h_min(järjend[0])
    saabumisaeg = h_min(järjend[1])
    hind = int(järjend[2])
    hinnad.append(hind)
    sõidu_kestvus = saabumisaeg - väljumisaeg
    sõidud.append(sõidu_kestvus)
lühim_kestvus = min(sõidud)
madalaim_hind = min(hinnad)
f.close()
f = open(fail)
järjekord = []
for rida in f:
    järjend = rida.split(" ")
    väljumisaeg = h_min(järjend[0])
    saabumisaeg = h_min(järjend[1])
    sõidu_kestvus = saabumisaeg - väljumisaeg
    hind = int(järjend[2])
    if sõidu_kestvus == lühim_kestvus or hind == madalaim_hind:
        järjekord.append(rida)
järjekord.sort()
for el in järjekord:
    print(el)
f.close()
