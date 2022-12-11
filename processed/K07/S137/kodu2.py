taks = open("taksohinnad.txt")
nimed = []
sisse = []
km = []
kulud = []
for rida in taks:
    a = 0
    km_hind = sisse_hind = takso_nimi = ''
    for täht in rida:
        if täht == ',':
            a = a + 1
            continue
        elif a == 0:
            takso_nimi = takso_nimi + täht
        elif a == 1:
            sisse_hind = sisse_hind + täht
        elif a == 2:
            km_hind = km_hind + täht
    nimed.append(takso_nimi)
    sisse.append(float(sisse_hind))
    km.append (float(km_hind))
taks.close()
sõidu_maa = float(input("Sisesta tee pikkus kilomeetrites: "))
pikkus = len(nimed)
i = 0
while i < pikkus:
    summa = sisse[i] + sõidu_maa * km[i]
    kulud.append(summa)
    i = i + 1
try:
    väike = min(kulud)
    väike = kulud.index(väike)
    print(f"Kõige odavam on {nimed[väike]}")
except:
    print("taksot pole")