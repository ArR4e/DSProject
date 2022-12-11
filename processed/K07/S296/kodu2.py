f = open("taksohinnad.txt","r", encoding="utf-8")
x = float(input("Sisesta tee pikkus kilomeetrites:"))
odavaim = 0
esimene = 0
try:
    for rida in f:
        if rida != "":
            lahku = rida.split(",")
            nimi = lahku[0]
            alg = lahku[1]
            km = lahku[2].strip()
            maksumus = (x * float(km)) + float(alg)
        if esimene == 0:
            esimene += 1
            odavaim=maksumus
        if maksumus <= odavaim:
            odavaim = maksumus
            o_nimi = nimi
    print("Kõige odavam on ",o_nimi)
except:
    print("Info puudub")
f.close()

