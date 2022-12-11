import film

def töötleKäsk(tähis, järjend = []):
    if tähis.upper() == "K":
        if film.loetleFilmid(järjend[0]) == []:
            print("Sellest žanrist filme ei leidunud!")
        else:
            print("Võimalikud filmid on:")
            for element in film.loetleFilmid(järjend[0]):
                print(element)
        return True
    elif tähis.upper() == "L":
        film.lisaFilm(" ".join(järjend[1:]), järjend[0])
        print("Film lisatud!")
        return True
    elif tähis.upper() == "V":
        film.kustutaFilm(" ".join(järjend[0:]))
        print("Film nimekirjast kustutatud! \nHead vaatamist!")
        return True
    else:
        return False

print("=== Filmiandmebaas ===")
print("Kuva filmid: K <žanr>")
print("Lisa film:   L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta:      E")
print("===")

while True:
    kasutaja_sisend = (input("> ")).split()
    käsk = töötleKäsk(kasutaja_sisend[0], kasutaja_sisend[1:])
    if not käsk:
        break
    