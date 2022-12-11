fail = open("kinganumbrid.txt", encoding="UTF=8")
pikkus=0
for rida in fail:
    try:
        pikkus = (2/3)*(float(rida) - 2)
        print(round(pikkus))
    except:
        print("vigane sisend")