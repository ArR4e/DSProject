def loetleFilmid(žanr):
    fail = open("filmid.txt", "r", encoding = "UTF-8")
    järjend = []
    for rida in fail:
        x = rida.strip()
        uusrida = x.split(" - ")
        if uusrida[1] == žanr:
            järjend.append(uusrida[0])
    fail.close()
    return järjend
    
def lisaFilm(nimi, žanr):
    fail = open("filmid.txt", "a", encoding = "UTF-8")
    fail.write("\n" + nimi + " - " + žanr)

def kustutaFilm(nimi):
    fail = open("filmid.txt","r", encoding = "UTF-8")
    sisu = fail.readlines()
    fail.close()
    fail = open("filmid.txt","w", encoding = "UTF-8")
    for rida in sisu:
        rida1 = rida.strip()
        rida2 = rida1.split(" - ")
        if rida2[0] != nimi:
            fail.write(rida1 + "\n")
    fail.close()
    
    
