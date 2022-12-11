def loetleFilmid(zanr):
    f = open("filmid.txt", "r", encoding = "UTF-8")
    l = []
    for r in f:
        if r == "\n":
            break
        uus = r.split(" - ")
        nimi = uus[0].strip()
        zanrts = uus[1].strip()
        if zanr == zanrts:
            l.append(nimi)
    f.close()
    return l
            
def lisaFilm(n,z):
    f = open("filmid.txt", "a",  encoding = "UTF-8")
    f.write(f"\n{n} - {z}\n")
    f.close()


def kustutaFilm(n):
    f = open("filmid.txt", "r", encoding = "UTF-8")
    u = f.readlines()
    f.close()
    y = open("filmid.txt", "w", encoding = "UTF-8")
    for i in u:
        if n != (i.split(" - ")[0]):
            y.write(i)
    f.close()