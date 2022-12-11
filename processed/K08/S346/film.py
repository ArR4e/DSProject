def algFilm():
    f = open("filmid.txt",)
    r = f.read()
    r = r.strip()
    r = r.split("\n")
    s = []
    for i in range(len(r)):
        a = r[i]
        a = a.split(" - ")
        s += a
    f.close()
    return s
def loetleFilmid(žanr):
    nimed = []
    a = algFilm()
    for i in a:
        while True:
            if i == žanr:
                i1 = a.index(i) - 1
                nimi = a[i1]
                nimi = nimi.strip()
                nimed += [nimi]
            else:
                break
    return nimed

def lisaFilm(nimi, žanr):
    rida = algFilm()
    nimi = "" + nimi
    rida += [nimi] + [žanr]
    c = 0
    x = int(len(rida)/2)
    f = open("filmid.txt", "w")
    for sõna in range(x):
        nimi = rida[c]
        c += 1
        žanr = rida[c]
        f.write("" + str(nimi) + " - " + str(žanr) + "\n")
        c += 1
    f.close()
def kustutaFilm(nimi):
    rida = algFilm()
    nimi = "" + nimi
    x = int(len(rida)/2)
    c = 0
    f = open("filmid.txt", "w")
    if nimi in rida:
        for sõna in range(x):
            if rida[c] == nimi:
                c += 2
            else:
                n = rida[c]
                c += 1
                z = rida[c]
                f.write("" + str(n) + "" + str(z) + "\n")
                c += 1
    f.close()