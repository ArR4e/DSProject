f = open("kinganumbrid.txt")
for rida in f:
    print(rida)
    kinganr = float(rida.strip())
    ümardatud_arv = round(kinganr, 2)
try:
    kinganr = "nelikümmend neli"
    pikkus = 2/3 * (kinganr) - 2
    pikkus = round(kinganr)
            print(pikkus)
            break
        except:
            print("Vigane sisend")

