# Erindite püüdmine failist lugemisel

fail = open("kinganumbrid.txt", encoding= 'UTF-8')

for rida in fail:
    try:
        kinganumber = float(rida)
        pikkus = round(2/3 * (kinganumber - 2))
        print(int(pikkus))
    except:
        print("Vigane sisend")