fail = open("filmid.txt", "r" , encoding="utf-8")
failiread = fail.readlines()
fail.close()

filmid = []

for rida in failiread:
    filmid.append(rida.strip("\n").lstrip().rstrip().rsplit(" - ", 1))


def loetleFilmid(žanr):
    nimed = []
    for rida in filmid:
        if rida[1].strip() == žanr:
            nimed.append(rida[0])
    return(nimed)

def lisaFilm(nimi, žanr):
    failkirjutajuurde = open("filmid.txt", "a" , encoding="utf-8")
    failkirjutajuurde.write("\n"+" "+ nimi+ " - "+ žanr)
    failkirjutajuurde.close()
    filmid.append([nimi, žanr])
    
def kustutaFilm(nimi):
    failkirjuta = open("filmid.txt", "w" , encoding="utf-8")
    i = 0
    for rida in filmid:
        if rida[0] == nimi:
            reanimi = rida
        else:
            if i==1:
                failkirjuta.write(("\n")+" "+rida[0]+" - "+rida[1])
            else:
                failkirjuta.write(" "+rida[0]+" - "+rida[1])
                i= 1
    filmid.remove(reanimi)
    failkirjuta.close()

