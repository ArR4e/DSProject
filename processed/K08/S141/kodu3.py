import film

def töötleKäsk(tähis, järjend):
    if tähis == "K":
        print("Võimalikud filmid on:")
        filmid = film.loetleFilmid(järjend)
        filmid = sõneks(filmid)
        print(filmid)
        
    elif tähis == "L":
        žarn = a[1]
        nimi = a[2:]
        nimi = sõneks(nimi)
        film.lisaFilm(nimi, žarn)
        print("Film lisatud!")
        
    elif tähis == "V":
        nimi = järjend
        nimi = sõneks(nimi)
        film.kustutaFilm(nimi)
        print("Film nimekirjast kustutatud!" + "\n" + "Head vaatamist!")
        
    else:
        tähis == "E"
        
def sõneks(järjend):
    sõne = ""
    for el in järjend:
        sõne += el + " "
    return sõne
        
print("FILMIANDMEBAAS".center(20) + "\n" + "Kuva filmid: K <žanr>" + "\n" + "Lisa film:   L <žanr> <film>" + "\n" + "Vaata filmi: V <filmi nimi>" + "\n" + "Lõpeta:      E" )    

while True:
    käsklus = str(input("Sisesta käsklus: "))
    a = käsklus.split()
    tähis = a[0]
    if tähis == "K":
        järjend = a[1]
        töötleKäsk(tähis, järjend)
    elif tähis == "L":
        järjend = a[1:]
        töötleKäsk(tähis, järjend)
    elif tähis == "V":
        järjend = a[1:]
        töötleKäsk(tähis, järjend)
    elif tähis == "E":
        break

    
