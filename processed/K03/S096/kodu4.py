# Erindite püüdmine failist lugemisel

f = open("kinganumbrid.txt", encoding="UTF-8")

for i in f:
    try:
        pikkus = round(2 / 3 * (float(i.strip())-2))
        print("Teie jalalaba pikkus on: " + str(pikkus))
    except:
        print("Vigane sisend")

f.close()
