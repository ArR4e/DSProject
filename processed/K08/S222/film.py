fail = open("filmid.txt")

filmid = []
for rida in fail:
    filmid.append(rida.strip().split(" - "))
fail.close()

def loetleFilmid(z):
    tagastada = []
    for film in filmid:
        if film[1] == z:
            tagastada.append(film[0])
    return tagastada
            
def lisaFilm(n,z):
    fail = open("filmid.txt","a")
    fail.write(n+" - "+z+"\n")
    filmid.append([n,z])
    fail.close()
    
def kustutaFilm(n):
    fail = open("filmid.txt","w")
    for film in filmid:
        if n == film[0]:
            filmid.remove(film)
    for film in filmid:
        fail.write(film[0]+" - "+film[1]+"\n")
    fail.close()
