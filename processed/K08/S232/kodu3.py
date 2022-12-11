import film

def töötleKäsk(tähis, järjend):
    if tähis == "E":
        return False
    elif tähis == "K":
        print("Võimalikud filmid on:")
        järjend = järjend[0]
        filmid = film.loetleFilmid(järjend)
        for filminimi in filmid:
            print(filminimi)
        return True
    elif tähis == "V":
        järjend = järjend[0]
        film.kustutaFilm(järjend)
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
        return True
    elif tähis == "L":
        lisatava_filmi_genre = järjend.pop(0)
        lisatava_filmi_nimi = str(" ".join(järjend))
        film.lisaFilm(lisatava_filmi_nimi, lisatava_filmi_genre)
        print("Film lisatud!")
        return True
    
print("=== FILMIANDMEBAAS ===")
print("Kuva filmid: K <žanr>")
print("Lisa film:   L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta:      E")
print("===")    

while True:
    sisestus = input("> ")
    sisestus = sisestus.split(" ")
    tähis = sisestus[0]
    sisestus.pop(0)
    järjend = sisestus
    if bool(töötleKäsk(tähis, järjend)) == False:
        break