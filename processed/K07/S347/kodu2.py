f = open("taksohinnad.txt", encoding="UTF=8" )
kilomeetreid = float(input("Sisesta teepikkus kilomeetrites:"))
taksode_hinnad = []
järjend2= []
for rida in f:
    b = rida.split(",")
    taksonimi = b[0]
    järjend2.append(taksonimi)
    stardihind = b[1]
    hind_kilomeetrile = b[2]
    hind = float(stardihind) + kilomeetreid * float(hind_kilomeetrile)
    taksode_hinnad.append(hind)
try:
    miinimum = taksode_hinnad[0]
    indeks = 0
    for i in range(len(taksode_hinnad)):
        if taksode_hinnad[i] < miinimum:
            miinimum =taksode_hinnad[i]
            indeks = i
    odavaim = järjend2[indeks]
    print(f"Kõige odavam takso on {odavaim}")
except:
    print("Hinnakiri puudub")
f.close()
