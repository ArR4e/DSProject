tee_pikkus = float(input("Sisesta tee pikkus kilomeetrites:"))
if tee_pikkus > 0:
    f = open("taksohinnad.txt")
    hinnad = []
    nimed = []
    for rida in f:
        info = rida.split(",")
        sisseistumise_hind = float(info[1])
        kilomeetri_hind = float(info[2])
        hind = sisseistumise_hind + kilomeetri_hind * tee_pikkus
        nimed = nimed + [info[0]]
        hinnad = hinnad + [hind]
    index = 0
    while True:
        if hinnad[0] == min(hinnad):
            index = 0
            break
        elif hinnad[1] == min(hinnad):
            index = index + 1
            break
        elif hinnad[2] == min(hinnad):
            index = index + 2
            break

    print("Kõige odavam on", nimed[index])
    f.close()
else:
    print("Proovige uuesti.")
