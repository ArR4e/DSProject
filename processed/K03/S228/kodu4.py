f = open("kinganumbrid.txt")

for kingasuurus in f:
    try:
        jalalaba_pikkus = 2/3 * (float(kingasuurus.strip()) - 2)
        print(round(jalalaba_pikkus))
    except:
        print("Vigane sisend.")
