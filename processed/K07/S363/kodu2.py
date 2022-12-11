f = open("taksohinnad.txt")

tee = float(input("Palun sisesta tee pikkus kilomeetrites: "))

hinnad = []
nimed = []

for i in f:
    rida = i.split(",")
    nimi = rida[0]
    sise = float(rida[1])
    hind = float(rida[2])
    
    kogu = sise + tee*hind
    hinnad.append(kogu)
    nimed.append(nimi)
        
if hinnad != []:
    firma = nimed[hinnad.index(min(hinnad))]
    print("Kõige odavam valik on",firma)
    
else:
    print("Vastust ei ole võimalik anda.")