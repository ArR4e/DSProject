distants = float(input("Sisestage tee pikkuse koju kilomeetrites: "))
f = open("taksohinnad.txt", encoding = "UTF-8")
taksod = []
takso_nimi = []
hinnad = []
for rida in f:
    taksod.append(rida.split(","))
for firma in taksod:
    takso_nimi.append(firma[0])
    hinnad.append(float(firma[1]) + distants*float(firma[2]))
try:
    x = hinnad.index(min(hinnad))
    print("Kõige odavam on", takso_nimi[x])
except:
    print("Mingi vea")
f.close()