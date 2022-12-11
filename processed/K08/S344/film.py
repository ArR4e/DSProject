import codecs
#f = open("filmid.txt", "r+")

def loetleFilmid(žanr):
    #print(žanr)
    f = codecs.open("filmid.txt", "r+", "utf-8")
    filmid = []
    for rida in f:
        osad = rida.split(" - ")
        nimi = osad[0].strip()
        tüüp = osad[1].strip()
        if žanr == tüüp:
            filmid.append(nimi)
        
    return filmid
    f.close()

def lisaFilm(nimi, žanr):
    f = codecs.open("filmid.txt", "a", "utf-8")
    f.write("\n" + nimi + " - " + žanr)
    f.close()        
            
def kustutaFilm(nimi):
    f = codecs.open("filmid.txt", "r", "utf-8")
    read = f.readlines()
    f.close()
    
    uus_fail = codecs.open("filmid.txt", "w", "utf-8")
    for rida in read:
        osad = rida.split("-")
        osaNimi = osad[0].strip()
        if osaNimi != nimi:
            uus_fail.write(rida)    
            
    uus_fail.close()


#print(loetleFilmid("märul"))
# lisa_film("AAAAA", "märul")
# kustutaFilm("AAAAA")