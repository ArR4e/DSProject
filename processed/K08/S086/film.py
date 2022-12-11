#Funktsioonid filmid.txt jaoks

def loetleFilmid(žanr):
    f = open("filmid.txt", encoding="UTF-8")
    nimekiri = f.readlines()
    f.close()
    žanri_filmid = []
    for film in nimekiri:
        film = film.replace("\n","").split(" - ")
        if film[1] == žanr:
            žanri_filmid.append(film[0])
    return žanri_filmid

def lisaFilm(nimi, žanr):
    f = open("filmid.txt", "a", encoding="UTF-8")
    f.write("\n" + nimi + " - " + žanr + "\n")
    f.close()
    
def kustutaFilm(nimi):
    f = open("filmid.txt", encoding="UTF-8")
    nimekiri = f.readlines()
    f.close()
    for film in nimekiri:
        if nimi in film:
            nimekiri.remove(film)
    f = open("filmid.txt", "w", encoding="UTF-8")
    for film in nimekiri:
        f.write(film)
    f.close()