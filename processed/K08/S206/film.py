fail = "filmid.txt"

def loetleFilmid(zanr):
    with open(fail, "r+", encoding="UTF-8") as f:
        a = []
        for rida in f:
            rida = rida.strip().split(" - ")
            if rida[1] == zanr:
                a.append(rida[0])
        return a
        
def lisaFilm(nimi, zanr):
    with open(fail, "r+", encoding="UTF-8") as f:
        a = f.readlines()
        if a == []:
            f.write(f"{nimi} - {zanr}")
        else:
             f.write(f"\n{nimi} - {zanr}")
    return
def kustutaFilm(nimi):
    with open(fail, "r+", encoding="UTF-8") as f:
        read = f.readlines()
        with open(fail, "w", encoding="UTF-8") as v:
            for rida in read:
                uus = rida.strip().split(" - ")
                if uus[0] != nimi:
                    v.write(f"{uus[0]} - {uus[1]} \n")
    return       
kustutaFilm("jee")