def loetleFilmid(zanr):
    tulemus = []
    with open("filmid.txt", "r", encoding="UTF-8") as f:
        for film in f:
            if zanr in film:
                tulemus.append(film[:film.index(' - ')])
    return tulemus      

def lisaFilm(nimi, zanr):
    with open("filmid.txt", "a", encoding="UTF-8") as f:
        f.write(f"\n{nimi} - {zanr}")
        
def kustutaFilm(nimi):
    uus_sisu = []
    with open("filmid.txt", "r", encoding="UTF-8") as f:
        for film in f:
            if nimi not in film:
                uus_sisu.append(film)
                
    with open("filmid.txt", "w", encoding="UTF-8") as f:    
        if uus_sisu != []:
            viimane = uus_sisu[-1]
            del uus_sisu[-1]
            
            for film in uus_sisu:
                f.write(film)
                
            f.write(viimane)