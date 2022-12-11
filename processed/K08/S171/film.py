def loetleFilmid(a):
    f = open("filmid.txt", "r")
    nimekiri = {}
    for rida in f:
        andmed = rida.strip().split(" - ")
        if andmed[1] not in nimekiri:
            nimekiri[andmed[1]] = [andmed[0]]
        else:
            nimekiri[andmed[1]].append(andmed[0])
    try:
        return nimekiri[a]
    except:
        return []
def lisaFilm(a,b):
    f = open("filmid.txt", "a")
    lisa = "\n" + a + " - " + b
    f.write(lisa)
    f.close()
def kustutaFilm(a):
    f = open("filmid.txt", "r")
    tekst = ""
    for rida in f:
        if a in rida:
            continue
        else:
            tekst += rida
    f.close()
    f = open("filmid.txt", "w") 
    f.write(tekst)
    f.close()
