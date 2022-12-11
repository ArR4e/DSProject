def tundmin(aeg):
    return 60*int(aeg[0:2])+int(aeg[3:5])
def kiirem(aeg1,aeg2):
    return tundmin(aeg1) < tundmin(aeg2)
def odavam(hind1, hind2):
    return int(hind1) < int(hind2)
#import
sp = []
with open(input("Sisestage failinimi: "), encoding="UTF-8") as fail:
    for rida in fail.readlines():
        sp += [rida.strip().split(" ")]
#sorteeri
for i in range(0, len(sp)-1):
        s = i
        for j in range(i, len(sp)):
            if tundmin(sp[j][0]) < tundmin(sp[s][0]):
                s = j
        sp[i], sp[s] = sp[s], sp[i]

valmis = False
while not valmis:
    sp2 = sp[:]
    if len(sp) == 1:
        break
    for i in range(0, len(sp)-1):
        if kiirem(sp[i][1],sp[i+1][1]):
            valmis = True
        elif odavam(sp[i][2],sp[i+1][2]):
            valmis = True
#ma otsisin 20 minutit bugi, lõpuks avastasin et polnud str intiks teinud ehk
# "10" < "8" edastas True :)
        else:
            sp2.pop(i)
            valmis = False
            break
    sp = sp2[:]

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for rida in sp:
    print(" ".join(rida))
