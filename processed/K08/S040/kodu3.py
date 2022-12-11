import film

print("=== FILMIANDMEBAAS ===")
print("Kuva filmid: K <žanr>")
print("Lisa film:   L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta:      E")
print("===")

info = input("> ")
jar = info.split(" ")

def töötleKäsk(info, jar):
    for jar[0] in jar:
        if jar[0] == "K":
            print("Võimalikud filmid on: ")
            return film.loetleFilmid(jar[1])
        elif jar[0] == "L":
            return film.lisaFilm(jar[2], jar[1])
            print("Film lisatud!")
        elif jar[0] == "V":
            return film.kustutaFilm(jar[2])
            print("Film nimekirjast kustutatud!")
        elif jar[0] == "E":
            return sys.exit()
    return töötleKäsk(info, jar)