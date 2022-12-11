
def loetleFilmid(genre):
    f = open("filmid.txt")
    b = []
    for i in f:
        a = i.strip().split(" - ")
        if genre == a[1]:
            b += [a[0]]
    return(b)
    f.close()
def lisaFilm(nimi,genre):
    f = open("filmid.txt","a")
    f.write(f"\n{nimi} - {genre}")
    f.close()
def kustutaFilm(nimi):
    f = open("filmid.txt","r")
    counter = 0
    c = f.readlines()
    for i in c:
        a = i.strip().split(" - ")
        if nimi == a[0]:
            c[counter] = ""
        counter += 1
    f.close()
    k = open("filmid.txt","w")
    k.writelines(c)
    k.close()
kustutaFilm("nimi")
            