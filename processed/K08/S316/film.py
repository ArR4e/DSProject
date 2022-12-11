def loetleFilmid(žanr):
    film = open("filmid.txt", encoding="UTF-8")
    filmide_nimekiri = []
    for rida in film:
        kriips = rida.split(" - ")
        nimi = kriips[0]
        teema = kriips[-1]
        teema = teema.strip()
        if žanr == teema:
            filmide_nimekiri.append(nimi)
    film.close()
    return filmide_nimekiri
    
def lisaFilm(nimi,žanr):
    film = open("filmid.txt","a",encoding="UTF-8")
    film.write("\n" + nimi + " - " + žanr)
    film.close()

def kustutaFilm(nimi):
    film = open("filmid.txt",encoding="UTF-8")
    sisu = ""
    for rida in film:
        filmid_list = list(rida.split(" - "))
        if nimi in filmid_list:
            continue
        else:
            sisu = sisu + rida
    film2 = open("filmid.txt","w",encoding="UTF-8")
    film2.write(sisu)     
    film.close()
    film2.close()