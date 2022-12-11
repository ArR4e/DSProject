f=open("taksohinnad.txt",  encoding='utf-8')

kaugus=float(input("Sisesta kui kaugel sa elad (kilomeetrites): "))
hind = 0
nimi=""

for rida in f:
    if rida == "":
        break
    takso = rida.split(",")
    summa = kaugus*float(takso[2])+float(takso[1])
    if summa < hind:
        hind = summa
        nimi = takso[0]
    elif hind == 0:
        hind = summa
        nimi = takso[0]
    
    
print("Odavaim on võtta takso nimega " + nimi + ", mis maksab kokku " + str(hind) + " eurot.")

