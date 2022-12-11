# küsi tee pikkust
kodutee = int(input("Sisesta tee pikkus kilomeetrites: "))
# loe andmed failist, salvesta järjendisse
taksohinnad = open("taksohinnad.txt", "r", encoding="UTF-8")
taksopakkujad = taksohinnad.readlines()
taksohinnad.close()


# abimuutujad, odavaima hinna suurus on
# esialgu ebarealistlikult suur, et seda
# saaks hiljem asendada väiksemate väärtustega
odavaim_pakkuja = ""
odavaim_hind = 2**63

# vaata kõiki taksohindu
for takso in taksopakkujad:
    pakkuja = takso.split(",")[0]
    sisseastumishind = float(takso.split(",")[1])
    kmhind = float(takso.split(",")[2])
    # vaata, kas hind on madalam
    # kui jah, määra praegune väärtus madalaimaks
    if sisseastumishind + kodutee * kmhind < odavaim_hind:
        odavaim_pakkuja = pakkuja
        odavaim_hind = sisseastumishind + kodutee * kmhind

# väljasta
print(f"Kõige odavam on {odavaim_pakkuja}.")