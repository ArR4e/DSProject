tee_pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
f = open("taksohinnad.txt", encoding = "UTF-8")

hinnad = []
nimed = []

for rida in f:
    if rida != "\n":
        andmed = rida.split(",")
        nimi = andmed[0].strip()
        istumine = float(andmed[1].strip())
        km = float(andmed[2].strip())
        hind = istumine+tee_pikkus*km
        hinnad.append(hind)
        nimed.append(nimi)

if len(hinnad) > 0 and tee_pikkus != 0:
    odavaim = min(hinnad)
    print("Odavaim on", nimed[hinnad.index(odavaim)])
    
    
    
    
    
    
    