tee = float(input("Sisesta tee pikkus kilomeetrites: "))

with open("taksohinnad.txt", "r", encoding="utf-8") as f:
    s_hind = 99999999999999999
    nimi = ""
    for i in f:
        i = i.strip("\n").split(",")
        hind = float(i[1]) + float(i[2])*tee
        if hind < s_hind:
            s_hind = hind
            nimi = i[0]
    print("Kõige odavam on", str(nimi) + ".")