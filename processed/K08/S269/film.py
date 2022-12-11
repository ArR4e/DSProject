def loetleFilmid(n):
    f = open("filmid.txt",encoding="utf-8")
    filmid = []
    for rida in f:
        if rida.strip().split(" - ")[-1] == n:
            filmid.append(rida.split(" - ")[0].strip())
    return filmid

def lisaFilm(f, z):
    fail = open("filmid.txt", "a", encoding="utf-8")
    fail.write("\n" + f + " - " + z)
    fail.close()
    
def kustutaFilm(f):
    fail = open("filmid.txt", "r", encoding="utf-8")
    out = ""
    for rida in fail:
        if f != rida.split(" - ")[0].strip():
            out += rida
    fail.close()
    fail = open("filmid.txt", "w", encoding="utf-8")
    fail.write(out)          
    fail.close()
    
    