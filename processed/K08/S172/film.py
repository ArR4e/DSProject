import io

def loetleFilmid(zanr):
    abilist = []
    f = io.open('filmid.txt', mode = "r", encoding = "UTF8")
    for rida in f:
        if rida.strip().endswith(zanr):
            rida = rida.split(' - ')
            rida[0] = rida[0].strip()
            abilist = abilist + [rida[0]]
    f.close()
    return abilist

def lisaFilm(nimi, zanr):
    lisa = '\n' + nimi + ' - ' + zanr 
    f = io.open('filmid.txt', mode = "a", encoding = "UTF8")
    f.write(lisa)
    f.close()

def kustutaFilm(nimi):
    f = io.open('filmid.txt', mode = "r+", encoding = "UTF8")
    read = f.readlines()
    f.truncate(0)
    for rida in read:
        if rida.strip().startswith(nimi):
            read.remove(rida)
        else:
            f.write(rida)
        
    f.close()