nimi="pekki"
žanr="märul"
film="Shrek"
filmid=[]
fail=open("filmid.txt", encoding="UTF-8")
for rida in fail:
    järj=[]
    y=rida.strip()
    x=y.split(" - ")
    filmid.append(x)
fail.close()
def loetleFilmid(žanr):
    järj=[]
    for rida in filmid:
        if žanr in rida:
            järj.append(rida[0])
    return järj
print(loetleFilmid(žanr))
f=open("filmid.txt", "a")
def lisaFilm(nimi, žanr):
    f.write(str(nimi) + " - " + str(žanr)+ "\n")
    f.close()
def kustutaFilm(film):
    for rida in filmid:
        if rida[0]==film:
            filmid.remove(rida)
    fail=open("filmid.txt", "w")
    for rida in filmid:
        f.write(str(rida[0])+ " - "+ str(rida[1]) +"\n")
    f.close()
kustutaFilm(film)