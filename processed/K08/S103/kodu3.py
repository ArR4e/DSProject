import film

print("""=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===""")

def töötleKäsk(tähis, järjend):
    if tähis == "K":
        filmid = film.loetleFilmid(järjend[0])
        print("Võimalikud filmid on:")
        for el in filmid:
            print(el)
        return True
    elif tähis == "L":
        film.lisaFilm(järjend[1],järjend[0])
        print("Film lisatud!")
        return True
    elif tähis == "V":
            film.kustutaFilm(järjend[0])
            print("Film nimekirjast kustutatud!")
            print("Head vaatamist!")
            return True
    elif tähis == "E":
        return False

while True:
    sisend = input("\n> ")
    j = []
    if len(sisend) > 1:
        sisend2 = sisend.split(" ")
        tähis1 = sisend[0]
        if tähis1 == "K" or tähis1 == "V":
            j.append(sisend[2:])
        elif tähis1 == "L":
            j.append(sisend2[1])
            indeks = len(sisend2[0]) + len(sisend2[1]) + 1
            j.append(sisend[indeks:])
    else:
        tähis1 = sisend
    tõeväärtus = töötleKäsk(tähis1, j)
    if tõeväärtus == False:
        break
    else:
        continue
