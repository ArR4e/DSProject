teepikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
odavaim = ""
hind = 0
i = 0

fail = open("taksohinnad.txt")

for rida in fail:
    info = rida.split(",")

    taksonimi = info[0]
    taksoistumine = float(info[1])
    taksokilomeeter = float(info[2])
    
    taksohind = taksoistumine + taksokilomeeter * teepikkus
    
    if i == 0:
        hind = taksohind
        odavaim = taksonimi
        
    elif taksohind < hind:
        hind = taksohind
        odavaim = taksonimi
    
    i += 1
    
print("Kõige odavaim on", odavaim)