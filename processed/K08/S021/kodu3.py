import film

# Kuva filmid: K <žanr>
# Lisa film:   L <žanr> <film>
# Vaata filmi: V <filmi nimi>
# Lõpeta:      E
sisend = input(str("Sisestage käsk ning tühikuga eraldatud argumendid: "))
sisendjärjend = sisend.split()
tähis = sisendjärjend[0]
nimijärjend = sisendjärjend[1:]
def töötleKäsk(tähis, järjend):
    if tähis == "K":
        žanr = nimijärjend[0]
        tulemus = film.loetleFilmid(žanr)
        if tulemus == []:
            print("Failis pole otsitud žanrist ühtegi filmi")
        else:
            print("Võimalikud filmid on:")
            i = 0
            while i < len(tulemus):
                kirjutatav = tulemus[i]
                i += 1
                print(kirjutatav)
            return True
    
    if tähis == "L":
        nimi = nimijärjend[1] + nimijärjend[2]
        žanr = nimijärjend[0]
        film.lisaFilm(nimi, žanr)
        print("Film lisatud")
        return True
    
    if tähis == "V":
        nimi = " ".join(nimijärjend)
        film.kustutaFilm(nimi)
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist")
        return True
    if tähis == "E":
        return False
töötleKäsk(tähis, nimijärjend)