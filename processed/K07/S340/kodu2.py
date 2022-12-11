teepikkus = input("Mis on teepikkus koju kilomeetrites: ")
teepikkus = float(teepikkus)

nimed = []
hinnad = []
f = open("taksohinnad.txt", encoding = "UTF-8")
for rida in f:
    jupid = rida.split(",")
    nimed = nimed + [jupid[0]]
    sisseistumine = jupid[1]
    kilomeeter = jupid[2]
    hinnad = hinnad + [float(sisseistumine) + teepikkus*float(kilomeeter)]
    
väikseim = min(hinnad)
indeks = hinnad.index(väikseim)
print(nimed[indeks])

f.close()