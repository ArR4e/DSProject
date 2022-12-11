def loetleFilmid(film):
    filmid = []
    with open("filmid.txt", encoding="utf-8") as f:
        for rida in f:
            if film in rida:
                filmid.append(rida.strip(f"{film}\n").split(" - ")[0])
        return filmid
        f.close()


def lisaFilm(film, žanr):
    with open("filmid.txt", "a", encoding="utf-8") as f:
        f.write(f"\n{film} - {žanr}")
    f.close()


#kõigepealt loeb ära, eemaldab listist filmi ja siis truncateib ja kirjutab kõik uuesti. Ühe korra "w+" avades huias ära kõik.
def kustutaFilm(film):
    with open("filmid.txt", "r", encoding="utf-8") as f:
        filmid = []
        for rida in f:
            filmid.append(rida)
    f.close
    
    with open("filmid.txt", "w", encoding="utf-8") as fail:
        for el in filmid:
            if not film in el:
                fail.write(el)
    f.close()
    