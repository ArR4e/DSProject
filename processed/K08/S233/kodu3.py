import film
def töötleKäsk(k, l):
    if k == "K":
        print("Võimalikud filmid on: ")
        for filmid in film.loetleFilmid(l[0]):
            print(filmid)
    elif k == "L":
        film.lisaFilm(l[0],l[1])
        print("Film lisatud!")
    elif k == "V":
        film.kustutaFilm(l[0])
        print("Film nimekirjast kustutatud! \nHead vaatamist!")
    elif k == "E":
        return False
    return True

while True:
    sisend = input(" Kuva filmid: K <žanr> \n Lisa film:   L <žanr> <film> \n Vaata filmi: V <filmi nimi> \n Lõpeta:      E \n")
    if sisend[0:1] == "K":
        jarjend = []
        jarjend.append(sisend[2: len(sisend)])
        filmid = töötleKäsk("K", jarjend)
            
    elif sisend[0:1] == "L":
        jarjend = []
        tyhik = sisend.find(" ", 2)
        žanr = sisend[2: tyhik]
        nimi = sisend[tyhik + 1: len(sisend)]
        jarjend.append(nimi)
        jarjend.append(žanr)
        töötleKäsk("L", jarjend)

    elif sisend[0:1] == "V":
        jarjend = []
        jarjend.append(sisend[2: len(sisend)])
        töötleKäsk("V", jarjend)
        
    elif sisend[0:1] == "E":
        break
