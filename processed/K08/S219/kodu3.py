import film

def töötleKäsk(tähis, argumendid = []):
    if tähis == "K":
        print(film.loetleFilmid(argumendid))
        return True
    if tähis == "L":
        film.lisaFilm(argumendid[0], argumendid[1])
        return True
    if tähis == "V":
        film.kustutaFilm(argumendid[0:])
        return True
    if tähis == "E":
        return False

print("=== FILMIANDMEBAAS ===")
print("Kuva filmid: K <žanr>")
print("Lisa film: L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta: E")

while True:
    käsklus = input("Sisesta käsklus: ")
    l = käsklus.split()

    if l[0] == "K":
        töötleKäsk(l[0], l[1])
        continue

    elif l[0] == "L":
        žanr = l[1]
        nimi = l[2:]
        uus = ' '.join(nimi)
        film.lisaFilm(uus, žanr)
        continue
        
    elif l[0] == "V":
        nimi = l[1:]
        uus = ' '.join(nimi)
        film.kustutaFilm(uus)
        
    elif l[0] == "E":
        töötleKäsk(l[0], [])
        break