fail = open(input("Fail: "),"r")
tekst = fail.readlines()
fail.close()

print(" Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
hea = []

aeg = []
hind = []
kokku = []

for el in range(len(tekst)):
    kokku.append(el)
    for i in range(len(tekst)-1):
        if int(tekst[i][0:5].replace(":","")) > int(tekst[i+1][0:5].replace(":","")):
            tekst[i+1],tekst[i] = tekst[i],tekst[i+1]
    
for i in tekst:
    aeg.append(float(i[6:8])-float(i[0:2])+float(i[9:11])/60-float(i[3:5])/60)
    hind.append(float(i.strip("\n").split()[-1]))

kesk_aeg = sorted(aeg)[len(kokku)//2]
kesk_hind = sorted(hind)[len(kokku)//2]

for i in range(len(kokku)):
    if hind[i] > kesk_hind or aeg[i] > kesk_aeg:
        kokku.remove(i)
        
for i in kokku:
    print(tekst[i].strip("\n"))