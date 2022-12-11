def loetleFilmid(žanr):
    f = open("filmid.txt", encoding = "UTF-8")
    sama = []
    for rida in f:
        a = rida.strip().split(" - ")
        if a[1] == žanr:
            liige = a[0]
            sama += [liige]
    return sama

def lisaFilm(žanr, nimi):
    f = open("filmid.txt", "a", encoding = "UTF-8")
    f.write("\n" + nimi + " - " + žanr)
    f.close()
        
def kustutaFilm(nimi):
    f = open("filmid.txt", "r", encoding = "UTF-8")
    tekst = f.readlines()
    for element in tekst:
        if nimi not in element:
            continue
        else:
            indeks = tekst.index(element)
            tekst.pop(indeks)
    f.close()
    print(tekst)
    f = open("filmid.txt", "w", encoding = "UTF-8")
    for film in tekst:
        f.write(film)
    f.close()