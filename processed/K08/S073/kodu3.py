import film

def töötleKäsk(cmd, args):
    if cmd == "K":
        movies = film.loetleFilmid(args[0])
        if movies:
            print("Võimalikud filmid on:")
            for i in movies:
                print(i)
        else: print("Filme pole, proovi uuesti!")
        return True

    if cmd == "L":
        if len(args) > 1:
            film.lisaFilm(" ".join(args[1:]), args[0])
            print("Lisatud!")
            return True
        print("Pole piisavalt argumente, proovi uuesti")
        return True

    if cmd == "V":
        film.kustutaFilm(" ".join(args))
        print("Kustutatud!")
        return True

    if cmd == "E":
        return False


print("""=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===""")

noexit = True
while noexit:
    a = input("> ")

    args = a.split(" ")
    res = töötleKäsk(args[0], args[1:])
    if not res:
        noexit = False