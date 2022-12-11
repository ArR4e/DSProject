
def loetleFilmid(žanr):
    nimekiri = open("filmid.txt", "r+", encoding = "UTF-8")
    järjend = nimekiri.read().replace("\n"," - ").split(" - ")
    filmide_loetelu = []
    for i in range(1,len(järjend),2):
        if järjend[i] == žanr:
            filmide_loetelu += [järjend[i-1]]
    nimekiri.close()
    return filmide_loetelu

def lisaFilm(nimi, žanr):
    nimekiri = open("filmid.txt", "a", encoding = "UTF-8")
    uus_rida = "\n" + str(nimi) + " - " + str(žanr)
    nimekiri.write(uus_rida)
    nimekiri.close()
    return uus_rida

def kustutaFilm(nimi):
    nimekiri = open("filmid.txt", "r+", encoding = "UTF-8")
    for rida in nimekiri:
        if rida.startswith(nimi):
            #rida = rida.replace(str(nimi) + " - ","")
            rida = rida.replace(str(nimi) + " - ","")
    #järjend = nimekiri.read().replace("\n"," - ").split(" - ")
    #indeks = järjend.index(nimi)
    #järjend.remove(järjend[indeks])
    #print(järjend)
    nimekiri.close()
    return 
