def loetleFilmid(zanr):
    f = open("filmid.txt")
    sisu = f.read()
    f.close()
    sisu = sisu.replace("\n", " ! ")
    sisu+=" ! "
    list = []
    s = ""
    for i in sisu:
        if i == "!":
            list.append(s)
            s = ""
        else:
            s+=i
    loendus = []
    for i in list:
        i = i.split()
        if i[-1] == zanr:
            i = i[:-2]
            i = " ".join(i)
            loendus.append(i)
    return loendus
    
def lisaFilm(nimi, zanr):
    f = open("filmid.txt","a")
    sisend = "\n"+nimi+" - "+zanr
    f.write(sisend)
    f.close()
    
def kustutaFilm(nimi):
    with open("filmid.txt") as f:
        sisu = f.readlines()
        uus_sisu = ""
        for i in sisu:
            if i.find(nimi) == -1:
                print(1)
                print(i)
                uus_sisu+=i
    with open("filmid.txt","w") as f:
        f.write(uus_sisu)