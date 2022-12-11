def loetleFilmid(žanr):
    otsitav = žanr
    with open("filmid.txt") as f:
        filmid = f.readlines()
    otsitavad = []
    for film in filmid:
        if otsitav in film:
            filmi_nimi = film.strip(" - {otsitav}")
            otsitavad = otsitavad + filmi_nimi
    return (otsitavad)
    
def lisaFilm(nimi,žanr):
    f = open('filmid.txt', 'a+')
    f.write("{nimi} - {žanr}","\n")
    f.close

def kustutaFilm(nimi):
    kustutada = nimi
    with open('filmid.txt','r') as f:
        filmid_ühekaupa = f.readlines()
    with open('filmid.txt','w') as f:
        for film in filmid_ühekaupa:
            if film.strip("\n") != (kustutada):
                f.write(film)
    