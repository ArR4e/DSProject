fail = open("taksohinnad.txt", "r", encoding = "UTF-8")
teepikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
taksod = []
hinnad = []
def taksohinnad():
    while True:
        rida = str(fail.readline().strip())
        if rida == "":
            break
        järjend = rida.split(",")
        takso = järjend[0]
        sisseastumine = float(järjend[1])
        kilomeeter = float(järjend[2])
        hind = sisseastumine + kilomeeter*teepikkus
        taksod.append(takso)
        hinnad.append(hind)
taksohinnad()
if taksod == [] or hinnad == []:
    print("Pole taksosid ega sõpru :)")
else:
    odavaim = min(hinnad)
    asukoht = int(hinnad.index(odavaim))
    print("Kõige odavam on", taksod[asukoht] + ".")
fail.close()