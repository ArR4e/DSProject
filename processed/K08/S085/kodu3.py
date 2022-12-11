import film
def töötleKäsk(käsk, järjend):
    if käsk.upper() == "K":
        print("Võimalikud filmid on:")
        filmid = järjend[0]
        for ele in film.loetleFilmid(filmid):
            print(ele)
    elif käsk.upper() == "L":
        print("Film lisatud!")
        žanr = järjend[0]
        nimi = ""
        nimi = " ".join(järjend[1:i])
        return film.lisaFilm(nimi, žanr)
    elif käsk.upper() == "V":
        print("Film nimekirjast kustutatud")
        print("Head vaatamist!")
        nimi = " ".join(järjend[0:i])
        return film.kustutaFilm(nimi)
    else:
        return False
print("=== FILMIANDMEBAAS ===")
print("Kuva filmid: K <žanr>")
print("Lisa film: L <žanr> <nimi>")
print("Vaata filmi: V <nimi>")
print("Lõpeta: E")
print("===")
while True:
    järjend = []
    a = input("> ")
    a = a.split(" ")
    if a[0] == "E":
        break
    i = 0
    for ele in a:
        i+= 1
    käsk = a[0]
    del a[0]
    järjend = a
    töötleKäsk(käsk, järjend)