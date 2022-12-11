
def loetleFilmid(zanr):
    fail1 = open("filmid.txt", "r", encoding="UTF-8")
    järjend = []
    while True:
        film = fail1.readline()
        film = film.strip()
        if film == "":
            break
        film = film.split(" - ")
        if zanr == film[-1]:
            järjend.append(film[0])
    fail1.close()        
    return järjend

def lisaFilm(nimi, zanr):
    fail2 = open("filmid.txt", "a", encoding="UTF-8")
    sisend = str(nimi) + " - " + str(zanr)
    fail2.write("\n" + sisend)
    fail2.close()
    return True

def kustutaFilm(kustutanimi):
    fail3 = open("filmid.txt", "r", encoding="UTF-8")
    lst = fail3.readlines()
    fail3.close()
    uusfail3 = open("filmid.txt", "w", encoding="UTF-8")
    
    for line in lst:
            if kustutanimi not in line:
                uusfail3.write(line)
    uusfail3.close()        
    return True
