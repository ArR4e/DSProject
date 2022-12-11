# Bussid

import datetime

f = open(input("Sisesta sõiduplaan: "), encoding="UTF-8")

bussiajad = {}
i = 0  #Unikaalne sõnastiku ID
hinnad = []
ajad = []
for rida in f:   #Käib faili läbi
    v, s, hind = rida.strip().split(" ")
    aeg = datetime.datetime.strptime(s, "%H:%M")-datetime.datetime.strptime(v, "%H:%M") #Leiab sõiduaja
    ajad.append(aeg)
    hinnad.append(int(hind))
    i += 1
    bussiajad[i] = v, s, int(hind), aeg  #Lisab sõnastiku bussiajad, hinna ja sõiduaja
f.close()

min_hind = min(hinnad)
min_aeg = min(ajad)
for i in bussiajad:  #Käib läbi bussiaegade sõnastiku ja väljastab lühima sõiduaja ja hinnaga bussid
    if min_aeg in bussiajad[i] or min_hind in bussiajad[i]:
        v, s, h, a = bussiajad[i]
        print(v, s, h)