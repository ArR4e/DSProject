def loetleFilmid(žanr):
    with open("filmid.txt", encoding="utf-8") as f:
        filmid=[]
        lines=f.read().splitlines()    
        for x in lines:
            film=x.partition(" - ")[0]
            liik=x.partition(" - ")[2]
            if liik==žanr:
                filmid.append(film)
        return filmid

def lisaFilm(nimi, žanr):
    with open("filmid.txt", "a+", encoding="utf-8") as f:
        f.write("\n")
        f.write(nimi)
        f.write(" - ")
        f.write(žanr)

def kustutaFilm(nimi):
    with open("filmid.txt", "r+", encoding="utf-8") as f:
        lines=f.readlines()
        for x in lines:
            if nimi in x:
                lines.remove(x)
    with open("filmid.txt", "w+", encoding="utf-8") as f:
        f.writelines(lines)
#https://stackoverflow.com/questions/15233340/getting-rid-of-n-when-using-readlines