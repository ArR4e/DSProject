import film
print("=== FILMIANDMEBAAS ==="+("\n")+"Kuva filmid: K <žanr>"+("\n")+"Lisa film:   L <žanr> <film>"+("\n")+"Vaata filmi: V <filmi nimi>"+("\n")+"Lõpeta:      E")

    
def töötleKäsk(tähis,järjend):
    if tähis == "K":
        print("Võimalikud filmid on:")
        for rida in film.loetleFilmid(järjend[0]):
            print(rida)
        return True
    elif tähis == "L":
        print("Film lisatud!")
        film.lisaFilm(" ".join(järjend[1:]),järjend[0])
        return True
    elif tähis == "V":
        print("Film nimekirjast kustutatud!"+("\n")+"Head vaatamist!")
        film.kustutaFilm(" ".join(järjend[0:]))
        return True
    elif tähis == "E":
        return False
while True:
    sisend = input()
    sisend = sisend.split()
    if len(sisend)==1:
        töötleKäsk(sisend[0],"a")
        break
    else:
        töötleKäsk(sisend[0],sisend[1:])