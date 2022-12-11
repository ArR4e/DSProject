def loetleFilmid(zharn):
    f = open("filmid.txt", "r", encoding = "UTF-8")
    loetelu = []
    for line in f:
        x = line.strip().split(" - ")
        if zharn == x[-1]:
            loetelu.append(x[0])
    f.close()
    return loetelu
print(loetleFilmid("märul"))

def lisaFilm(nimi, zharn):
    f = open("filmid.txt", "a", encoding = "UTF-8")
    f.write("\n" + nimi + " - " + zharn)
    f.close()

def kustutaFilm(nimi):
    f = open("filmid.txt", "r", encoding="UTF-8")
    filmid = f.readlines()
    for film in filmid: 
        if film.split(" - ")[0] == nimi: 
                filmid.remove(film)
    f.close()
   
    f = open("filmid.txt", "w", encoding="UTF-8")
    length = len(filmid)
    for index,film in enumerate(filmid):
        if not index == length - 1:
            f.write(film)
        else:
            f.write(film.strip())
    f.close()