teepikkus = float(input("Sisesta tee pikkus kilomeetrites:"))
fail = open("taksohinnad.txt", "r", encoding="UTF-8")
nimed=[]
hinnad=[]
for rida in fail:
    rida = rida.strip().split(",")
    nimi = rida[0]
    sisse = float(rida[1])
    km = float(rida[2])
    hind = sisse + km*teepikkus
    hinnad.append(hind)
    nimed.append(nimi)
    

x = min(hinnad)
indeks = hinnad.index(x)
y = nimed[indeks]

print("Kõige odavam on" ,y+".")

fail.close