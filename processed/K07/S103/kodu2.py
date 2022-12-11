teepikkus = input("Sisesta tee pikkus kilomeetrites: ")

fail = open("taksohinnad.txt", encoding="UTF-8")
hinnad = []
nimed = []
for rida in fail:
    realt = rida.strip().split(",")
    hind = float(realt[1]) + float(realt[2])*float(teepikkus)
    hinnad.append(hind)
    nimed.append(realt[0])

try:
    taksonimi = (nimed[hinnad.index(min(hinnad))])
    print("Kõige odavam on", taksonimi)

except:
    print("Taksot ei leitud")
