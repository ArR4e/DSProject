def takso_hind(takso_info):
    takso_hind = float(takso_info[1]) + teepikkus * float(takso_info[2])
    return takso_hind

fail = open("taksohinnad.txt", encoding = "UTF-8")

teepikkus = float(input("Sisesta tee pikkus kilomeetrites: "))

takso_hinnad = []
takso_firmad = []
try:
    while True:
        takso = fail.readline().split(",")
        if takso == [""]:
            break
        takso_hind_õige = takso_hind(takso)
        takso_hinnad.append(takso_hind_õige)
        takso_firmad.append(takso[0])

    odavaim_hind = min(takso_hinnad)
    odavaima_hinna_indeks = takso_hinnad.index(odavaim_hind)
    odavaim_firma = takso_firmad[odavaima_hinna_indeks]
    
    print("Kõige odavam on " + odavaim_firma + ".")
except:
    print("Sisestatud fail on tühi.")



