tabel=[]
f = open("taksohinnad.txt", encoding = "UTF-8")
for rida in f:
    takso = []
    osad = rida.split(",")
    for osa in osad:
        takso.append(osa.strip("\n"))
    tabel.append(takso)
f.close()
pikkus = float(input("Sisestage tee pikkus: "))
if len(tabel) == 0:
    print("fail on tühi")
else:
    odavaim = 0
    kokku = 0
    jär=[]
    for el in tabel:
        jär.append(float(el[1]) + float(el[2]) * pikkus)
    minimaalne = (min(jär))
    indeks = jär.index(minimaalne)
    print(tabel[indeks][0])
