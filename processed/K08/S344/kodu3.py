import film


def töötleKäsk(sisend, järjend):
    if sisend == "K":
        print("Võimalikud filmid on: ")
        for f in film.loetleFilmid(järjend[0]):
            print(f)
        return True
    if sisend == "L":
        film.lisaFilm(järjend[0], järjend[1])
        print("Film lisatud!")
        return True
    if sisend == "V":
        film.kustutaFilm(järjend[0])
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
        return True
    if sisend == "E":
        return False
    else:
        return True

#töötleKäsk("V", ["AAAAAA", "BBBBB"])

print("Filmiandmebaas")
print("Kuva filmid: K <žanr>")
print("Lisa film:   L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta:      E")
print("====", "\n")

while True:
    a = input("> ")
    if a[0:1] == "K":
        r = töötleKäsk("K", [a[2:]])
    elif a[0:1] == "L":
        žanr = str(a[2:a[2:].find(' ')+2])
        filminimi = str(a[3 + len(žanr):])
        r = töötleKäsk("L", [filminimi, žanr])
    elif a[0:1] == "V":
        r = töötleKäsk("V", [a[2:]])
    else:
        r = töötleKäsk(a[0:1], [])
    if r == False:
        break