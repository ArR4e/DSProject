teepikkus = float(input("Sisesta teepikkus kilomeetrites: "))
taksod = []
with open("taksohinnad.txt") as f:
    for i in f:
        taksod.append(list(i.strip().split(",")))

if len(taksod) > 0:
    def hind(jr_nr):
        global teepikkus
        sisse = float(taksod[jr_nr][1])
        km = float(taksod[jr_nr][2])
        return sisse + km*teepikkus
    
    odav = hind(0)
    for i in range(len(taksod)):
        uus = hind(i)
        if min(uus, odav) == uus:
            odav = uus
            odav_nimi = taksod[i][0]
    
    print("Kõige odavam on " + odav_nimi + ".")