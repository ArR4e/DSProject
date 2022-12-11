f = open("filmid.txt", encoding = "UTF-8")
file = f.readlines()

def loetleFilmid(x):
    filmid = []
    vastus = []
    read = f.readlines()
    for rida in read:
        filmid.append(rida.strip())
    for sõna in filmid:
        if sõna.endswith(x) == True:
            vastus.append(sõna.strip(" - " + x))
    return vastus
        
        
def lisaFilm(x, y):
    f = open("filmid.txt", "a", encoding = "UTF-8")
    f.write("\n" + x + " - " + y )
    
def kustutaFilm(x):
    f = open("filmid.txt", "w", encoding = "UTF-8")
    for i in range(len(file)):
        rida = file[i]
        if not rida.startswith(x) == True:
            f.write(rida)

kustutaFilm("Shrek")