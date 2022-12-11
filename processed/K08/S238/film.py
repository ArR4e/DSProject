def loetleFilmid(zanr):
    alist = []
    for el in filmlist:
        if el.endswith(zanr):
            el = el.split(" - "+zanr)
            alist.append(el[0])
    return alist

def lisaFilm(nimi,zanr):
    pealkiri = nimi + " - " +zanr

    f.write(pealkiri)
    f.write("\n")
    return "Lisasin faili filmi: " + pealkiri

def kustutaFilm(nimi):
    for el in a:
        if el.startswith(nimi):
            del a[a.index(el)]
    for el in a:
        del a[a.index(el)]
        f.write(el)
            
            

    
f = open("filmid.txt","r+", encoding="UTF-8")

filmlist = []
a = []


for rida in f:
    rida = rida.strip()
    filmlist.append(rida)
    

print(loetleFilmid("multikas"))



f.close()
