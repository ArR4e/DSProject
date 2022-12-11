def loetleFilmid(žanr):
    f = open("filmid.txt", encoding="utf-8")
    žanri_filmid = []
    for rida in f:
        film = rida.strip().split(" - ")
        if film[1] == žanr:
            žanri_filmid.append(film[0])
    f.close()
    return žanri_filmid

def lisaFilm(filmi_nimi, filmi_žanr):
    f = open("filmid.txt", "a", encoding="utf-8")
    f.write(f"\n{filmi_nimi} - {filmi_žanr}")
    f.close()

def kustutaFilm(nimi):
    f = open("filmid.txt", encoding="utf-8")
    fail = f.readlines()
    f.close()
    f = open("filmid.txt", "w", encoding="utf-8")
    for rida in fail:
        film = rida.strip().split(" - ")
        if film[0] != nimi:
            f.write(rida)
    f.close()