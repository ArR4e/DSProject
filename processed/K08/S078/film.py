def loetleFilmid(žanr):
    with open("filmid.txt", 'r+', encoding="UTF-8") as f:
        fail = f.readlines()
    
    x = 0
    film_žanriga = []
    filmi_nimi = []
    
    for i in fail:
        if žanr in i:
            film_žanriga += i.split(" - ")
            filmi_nimi.append(film_žanriga[x])
            x += 2
            
    return filmi_nimi

def lisaFilm(nimi, žanr):
    with open("filmid.txt", 'a', encoding="UTF-8") as f:
        f.write("\n" + nimi + " - ")
        f.write(žanr)
    
def kustutaFilm(nimi):
    with open("filmid.txt", 'r+', encoding="UTF-8") as f:
        fail = f.readlines()
    for i in fail:
        if nimi in i:
            fail.remove(i)
    with open("filmid.txt", 'w', encoding="UTF-8") as f:
        for i in fail:
            f.write(i)
