# 2. Filmide nimekiri

def loetleFilmid(žanr):
    filmid = []
    fail = open("filmid.txt", "r", encoding = "UTF-8")
    for rida in fail:
        a = rida.split(" - ")
        nimi = (a[0])
        ža = ((a[1].split('\n'))[0])
        if ža == žanr:
            filmid.append(nimi)
    fail.close()
    return filmid

def lisaFilm(nimi, žanr):
    nimižanr = nimi + " - " + žanr
    with open("filmid.txt", "a", encoding = "UTF-8") as f: 
        f.writelines("\n" +nimižanr)
        f.close()
    
    
def kustutaFilm(nimi):
    with open("filmid.txt", "r", encoding = "UTF-8") as f:
        lines = f.readlines()
        f.close()
    n = 0
    for line in lines:
        rea = lines[n]
        a = line.split(" - ")
        nimi1 = (a[0])
        if nimi == nimi1:
            indeks = lines.index(rea)
            del lines[indeks]
        n = n + 1
    new_f = open("filmid.txt", "w+", encoding = "UTF-8")
    for line in lines:
        new_f.write(line)    
    new_f.close()
    
#nimi = 'Moana'
#žanr = 'ajalugu'
#loetleFilmid(žanr)
#lisaFilm(nimi, žanr)
#kustutaFilm(nimi)