def loetleFilmid(a) :
    f = open("filmid.txt", encoding="UTF-8")
    filmid = []
    žanrid = []
    while True:
        for rida in f:
            rea_osad = rida.split(" - ")
            film = str(rea_osad[0])
            žanr = str(rea_osad[1]).strip("\n")
            if a == žanr:
                filmid = filmid + [film.strip(" ")]
            žanrid = žanrid + [žanr]
            if film == "":
                break
        return filmid
    f.close()
    
def lisaFilm(a, b) :
    #a = input("Sisesta filmi nimi: ")
    #b = input("Sisesta filmi žanr: ")
    with open("filmid.txt", "a") as f:
        f.write("\n" + a + " - " + b)
    
    f.close()

def kustutaFilm(nimi) :
    f = open("filmid.txt", encoding="ISO-8859-1")
    content = ""
    for rida in f:
        filmid = list(rida.split(" - "))
        print(filmid)
        if nimi in filmid:
            continue
        else:
            content = content + rida
    f2 = open("filmid.txt", "w", encoding="ISO-8859-1")
    f2.write(content)
    f.close()
    f2.close()