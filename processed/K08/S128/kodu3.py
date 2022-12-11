#Juku filmiandmebaas
import film

def töötleKäsk(tähis,järjend):
    if tähis == "K":
        print("> " + tähis + " " + järjend)
        print("Võimalikud filmid on:")
        genre_films = film.loetleFilmid(järjend)
        for i in range(len(genre_films)):
            print(genre_films[i])
        return True
    
    elif tähis == "L":
        järjend = järjend.split(" ")
        if len(järjend) > 2:
            for i in range(1, len(järjend), 2):
                filminimi = ' '.join([järjend[i], järjend[i+1]])
        else:
            filminimi = järjend[1]
        print("> " + tähis + " " + järjend[0] + " " + filminimi)
        film.lisaFilm(filminimi, järjend[0])
        print("Film lisatud!")
        return True
    
    elif tähis == "V":
        print("> " + tähis + " " + järjend)
        film.kustutaFilm(järjend)
        print("Film nimekirjast kustutatud!\n" + "Head vaatamist!")
        return True
    
    elif tähis == "E":
        print("> " + tähis)
        return False

print("=== FILMIANDMEBAAS ===")
print("Kuva filmid: K <žanr>")
print("Lisa film:   L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta:      E")
print("===" + "\n")

while True:
    küsimus = input()
    täht = küsimus[0]
    sisu = küsimus[2:]
    if töötleKäsk(täht, sisu):
        continue
    else:
        break