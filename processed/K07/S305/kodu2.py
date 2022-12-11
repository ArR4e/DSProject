p = float(input("Sisesta tee pikkus kilomeetrites: "))
f = open("taksohinnad.txt")
hinnad = []
taksod = []
try:
    for rida in f:
        rida = rida.strip("\n")
        rida1 = tuple(rida.split(","))
        hind = float(rida1[1]) + float(rida1[2]) * p
        taksod = taksod + [rida1[0]]
        hinnad = hinnad + [hind]
    print("Kõige odavam on " + taksod[hinnad.index(min(hinnad))])
except ValueError:
    print("Tühi hinnakiri.")