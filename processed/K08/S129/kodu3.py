import film

print("""=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===========================
""")


def töötleKäsk(tähis, järjend):
    if tähis == "K":
        print("Võimalikud filmid on:")
        x = film.loetleFilmid(järjend[0])
        for el in x:
            print(el)
        
    elif tähis == "L":
        film.lisaFilm(" ".join(järjend[1:len(järjend)]), järjend[0])
        print("Film lisatud!")
    
    elif tähis == "V":
        film.kustutaFilm(" ".join(järjend[1:len(järjend)]))
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
        
    else:
        print("Sisesta korrektne käsk")


while True:
    sisse = input().split()
    if sisse[0] == "E":
        break
    
    käsud = [x for x in sisse[1:len(sisse)]]
    töötleKäsk(sisse[0], käsud)
    