import film
def töötleKäsk(tahis,argumendid):
    if tahis == "K":
        nimekiri = film.loetleFilmid(argumendid[1])
        print("Võimalikud filmid on:")
        for el in nimekiri:
            print(el)
    elif tahis == "L":
        film.lisaFilm(argumendid[2],argumendid[1])
        print("Film lisatud!")
    elif tahis == "V":
        film.kustutaFilm(argumendid[1])
        print("Film nimekirjast kustutuatud!")
        print("Head vaatamist!")
    else:
        return False
    return True
print("=== FILMIANDMEBAAS ===")
print("Kuva filmid: K <žanr>")
print("Lisa film: L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta: E")
print("===")

while True:
    sisend = input("> ")
    jarjend = []
    jarjend = sisend.split(" ")
    if jarjend[0] == "L":
        jarjend[2] = ' '.join(jarjend[2:])
    elif jarjend[0] == "V":
        jarjend[1] = ' '.join(jarjend[1:])
    if töötleKäsk(jarjend[0],jarjend) == False:
        break