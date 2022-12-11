def loetleFilmid(tyyp):
    nimi=[]
    zanr=[]
    valik=[]
    fail=open("filmid.txt", "r", encoding="UTF-8")
    for rida in fail:
        rida = rida.strip()
        rida = rida.split(" - ")
        nimi.append(rida[0])
        zanr.append(rida[1])
    fail.close()
    #print(zanr)
    #print(nimi)
    #print(tyyp)
    for rida in zanr:
        if tyyp in rida:
            valik.append(nimi[zanr.index(rida)])
    return valik
            
def lisaFilm(nimi, zanr):
    fail=open("filmid.txt", "a", encoding="UTF-8")
    s= ("\n" + nimi + " - " + zanr)
    fail.write(s)
    fail.close()
    return
    
    
def kustutaFilm(film):
    with open("filmid.txt","r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if film not in line:
                f.write(line)
        f.truncate()
    return
    