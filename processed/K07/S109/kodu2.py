pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
fail = open('taksohinnad.txt', encoding="UTF-8")

hinnad = []
nimed = []
for rida in fail:
    järj = rida.split(',')
    nimi = järj[0]
    alustamine = float(järj[1])
    km = float(järj[2])
    hind = alustamine + pikkus*km
    hinnad.append(hind)
    nimed.append(nimi)

print(hinnad)
print(nimed)

väikseim = min(hinnad)
indeks = hinnad.index(väikseim)
x = nimed[indeks]

print("Kõige odavam takso on", x)
        
fail.close()