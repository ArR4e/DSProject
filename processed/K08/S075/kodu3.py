import film
def töötleKäsk(tähis,järjend):
    if tähis=="K":
        esimene=film.loetleFilmid(järjend[0])
        print("Võimalikud filmid on: ")
        for nimi in esimene:
            print(nimi) 
    elif tähis=="L":
        teine=film.lisaFilm(järjend[1], järjend[0])
        print("Film lisatud!")
    elif tähis=="V":
        kolmas=film.kustutaFilm(" ".join(järjend))
        print("Film nimekirjast kustutatud! \nHead vaatamist!")
    elif tähis=="E":
        return False
    else:
        return True
    
print("=== FILMIANDMEBAAS ==="+"\n"+"Kuva filmid: K <žanr>"+"\n"+
      "Lisa film: L <žanr> <film> \nVaata filmi: V <filmi nimi> \nLõpeta: E \n=== \n" )
a=input("> ").split(" ")


töötleKäsk(a[0], a[1:])