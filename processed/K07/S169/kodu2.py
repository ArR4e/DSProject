fail = open("taksohinnad.txt", "r", encoding="utf8")
taksod = []
teepikkus = float(input("Sisesta tee pikkus kilomeetrites: "))

for a in fail.readlines():
    taksod.append(a.strip())

nimi_hinnad = {}
hinnad = []
for i in taksod:
    nimi = i.split(",")[0]
    istumisehind = i.split(",")[1]
    km_hind = i.split(",")[2]
    hind = float(istumisehind) + float(km_hind) * teepikkus
    nimi_hinnad[hind] = nimi
    hinnad.append(hind)

try:
    print("Kõige odavam on", nimi_hinnad[min(hinnad)])
except:
    print("Tekkis mingi probleem")
    