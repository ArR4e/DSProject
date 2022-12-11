def loetleFilmid(žanr):
    filmid = open("filmid.txt", "r", encoding="utf-8")
    filmid_uus = filmid.readlines()
    nimekiri = []
    for rida in filmid_uus:
        if žanr in rida:
            rida_uus = rida.replace("\n","").replace(žanr, "").replace(" - ", "")
            nimekiri += [rida_uus]  
    filmid.close()
    return nimekiri

#print(loetleFilmid("multikas"))

def lisaFilm(nimi, žanr):
    filmid = open("filmid.txt", "a", encoding="utf-8")
    filmid.write("\n" + str(nimi) + " - " + str(žanr)) 
    filmid.close()
    
#print(lisaFilm("Üksinda kodus", "komöödia"))

def kustutaFilm(nimi):
    filmid = open("filmid.txt", "r", encoding="utf-8")
    sisu = filmid.readlines()
    filmid.close()
    
    filmid_uus = open("filmid.txt", "w", encoding="utf-8")
    for rida in sisu:
        if nimi not in rida:
            filmid_uus.write(rida)
    filmid_uus.close()
    
#print(kustutaFilm("Üksinda kodus"))