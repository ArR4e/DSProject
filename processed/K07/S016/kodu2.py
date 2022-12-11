f = open("taksohinnad.txt", encoding = "UTF-8")

valikud = []
km = float(input("Sisesta km: "))
if km == "0":
    while True:
        rida = f.readline()
        if rida == "":
            break
        ridasplit = rida.split(",")
        takso_nimi = ridasplit[0]
        taksofirmade_nimekiri.append(takso_nimi)
        sisseistumisehind = float(ridasplit[1])
        km_hind = float(ridasplit[2])
        hind = sisseistumisehind
        #print(hind)
        valikud.append(hind)
else:
    taksofirmade_nimekiri = []
    while True:
        rida = f.readline()
        if rida == "":
            break
        ridasplit = rida.split(",")
        takso_nimi = ridasplit[0]
        taksofirmade_nimekiri.append(takso_nimi)
        sisseistumisehind = float(ridasplit[1])
        km_hind = float(ridasplit[2])
        hind = sisseistumisehind + km_hind * km
        #print(hind)
        valikud.append(hind)

try:
    odavaim = min(valikud)
    järk = valikud.index(odavaim)
    väljund_lõpuks = taksofirmade_nimekiri[järk]
    print("Kõige odavam on ", väljund_lõpuks)
except:
    print()
f.close()