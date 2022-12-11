tee = float(input("Siseta tee pikkus kilomeetrites: "))
f = open("taksohinnad.txt", "r", encoding="utf8")
parim = ""
for loen in f:
    loen = f.readline
    rida = loen.split(",")
    hind = str(rida[1]) + str(rida[2])*str(tee)
    if hind > parim:
        parim = rida[0]
print("Odavaim on "+ str(parim))
f.close()