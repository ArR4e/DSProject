import film

def töötleKäsk(käsk, järjend=[]):
    if käsk[0] == "K":
        print("Võimalikud filmid on:\n" + "\n".join(film.loetleFilmid(käsk[1])))
        return True

    if käsk[0] == "L":
        tähis = "L"
        zanr = käsk[1]
        filmi_nimi = " ".join(käsk[2:])
        
        film.lisaFilm(filmi_nimi, zanr)
        print("Film lisatud!")
        return True
        
    if käsk[0] == "V":
        film.kustutaFilm(käsk[1])
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
        return True
        
    if käsk[0] == "E":
        return False


print("""=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===""")


käsk = input("").split(" ")

while töötleKäsk(käsk) == True:
    käsk = input("").split(" ")