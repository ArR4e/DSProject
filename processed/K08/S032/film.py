def loetleFilmid(žanr):
    f = open("filmid.txt", encoding = "UTF-8")
    filmid = []
    for rida in f.readlines():
        film = rida.strip().split(' - ')
        if film[1] == žanr:
            filmid.append(film[0])
    f.close()
    return filmid

def lisaFilm(nimi, žanr):
    f = open("filmid.txt", 'a', encoding = "UTF-8")
    f.write("\n" + nimi + " - " + žanr)
    f.close()
    
    
def kustutaFilm(nimi):
    f = open("filmid.txt", 'r+', encoding = "UTF-8")
    tulemus = ""
    for rida in f.readlines():
        if nimi in rida:
            continue
        tulemus += rida
    f.seek(0)
    f.truncate()
    f.write(tulemus)
    f.close()
    
#print(loetleFilmid('märul'))
#kustutaFilm("Spider-Man")