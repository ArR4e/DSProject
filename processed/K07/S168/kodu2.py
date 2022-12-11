while True:
    try:
        km = float(input("Sisesta tee pikkus kilomeetrites: "))
        break
    except:
        pass

try:
    hindade_list = []
    fail = open("taksohinnad.txt", encoding = 'utf-8')
    for rida in fail:
        rida = rida.strip()
        rida = rida.split(',')
        takso_nimi = rida[0]
        sisseistumise_hind = float(rida[1])
        km_hind = float(rida[2])
        kogu_hind = sisseistumise_hind + km * km_hind
        hindade_list.append(kogu_hind)
        if kogu_hind <= min(hindade_list):
            parim_takso = takso_nimi
    fail.close()

    print("Kõige odavam on " + parim_takso)
except:
    pass
