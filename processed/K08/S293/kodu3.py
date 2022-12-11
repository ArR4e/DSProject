import film

print("""Kuva filmid: K <žanr>\n
Lisa film:   L <žanr> <film>\n
Vaata filmi: V <filmi nimi>\n
Lõpeta:      E""")


def töötleKäsk(käsk, sõne):
    if käsk=="K":
        print("Võimalikud filmid on:")
        filmid=film.loetleFilmid(sõne)
        for i in range(len(filmid)):
            print(filmid[i])
        return True
    if käsk=="L":
        järjend=sõne.split(" ",1)
        film.lisaFilm(järjend[1], järjend[0])
        print("Film lisatud!")
        return True
    if käsk=="V":
        film.kustutaFilm(x[1])
        print("Film kustutatud!")
        print("Head vaatamist!")
        return True
    if käsk=="E":
        return False
        

while True:
    x=input().split(" ",1)
    if len(x)==1:
        käsk=x[0]
    else:
        käsk=x[0]
        sõne=x[1]
    if töötleKäsk(käsk,sõne)==False:
        break
    else:
        continue

    