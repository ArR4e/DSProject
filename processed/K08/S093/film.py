def loetleFilmid(zanr):
    fail = open('filmid.txt', 'r', encoding="UTF-8")
    for sisu in fail.readlines():
        uus_sisu = sisu.replace("\n", "").split(' - ')
        movie = uus_sisu[0]
        zanr_0 = uus_sisu[1]
        if (zanr_0 == zanr):
            print(movie)
    fail.close()

def lisaFilm(film, zanr):
    fail = open('filmid.txt', 'a', encoding="UTF-8")
    fail.write("\n " + film + " - " + zanr)
    fail.close()
    
def kustutaFilm(nimi):
    with open('filmid.txt', 'r', encoding="UTF-8") as file:
        lin = f.readlines()
        file.close()
    n = 0
    for line in lin:
        rea = lines [n]
        a = line.split(' - ')
        nimi_1 = (a[0])
        if nimi == nimi_1:
            ind = lin.index(rea)
            del lin[ind]
        n = n + 1
        new = open('filmid.txt', 'w+', encoding="UTF-8")
        for line in lin:
            new.write(line)
            new.close()
            

    
    

