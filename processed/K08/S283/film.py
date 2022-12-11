def loetleFilmid(žanr):
    järjend = []
    soovižanr = []
    f = open("filmid.txt", encoding="UTF-8")
    for rida in f:
        järjend = rida.strip().split(" - ")
        if järjend[1] == žanr:
            soovižanr.append(järjend[0])
    f.close()
    return soovižanr
    
def lisaFilm(nimi, žanr):
    f = open("filmid.txt", "a", encoding="UTF-8")
    f.write("\n " + nimi + "- " + žanr)
    f.close()

def kustutaFilm(nimi):
    järjend = []
    f = open("filmid.txt", encoding="UTF-8")
    faili_sisu = f.readlines()
    f.close()
    f = open("filmid.txt", "w", encoding="UTF-8")
    for rida in faili_sisu:
        järjend = rida.strip().split(" - ")
        if järjend[0] != nimi:
            f.write(rida)                    
    f.close()