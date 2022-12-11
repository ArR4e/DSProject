import film
def töötleKäsk(tähis, järjend):
    if tähis == 'K':
        žanr1 = järjend[0]
        järjekord1 = film.loetleFilmid(žanr1)
        n = 0
        print("Võimalikud filmid on: ")
        while n < len(järjekord1):
            print(järjekord1[n])
            n += 1
        return True
    elif tähis == 'L':
        žanr2 = järjend[0]
        nimi2 = ' '.join(järjend[1:])
        järjekord2 = film.lisaFilm(nimi2,žanr2)
        print("Film lisatud!")
        return True
    elif tähis == 'V':
        nimi3 = ' '.join(järjend[0:])
        järjekord3 = film.kustutaFilm(nimi3)
        print("Film nimekirjast kustutatud!"+"\n"+"Head vaatamist!")
        return True
    elif tähis == 'E':
        return False
       
print("=== FILMIANDMEBAAS ==="+"\n"+"Kuva filmid: K <žanr>"+"\n"+"Lisa film:   L <žanr> <film>"+"\n"+"Vaata filmi: V <filmi nimi>"+"\n"+"Lõpeta:      E "+"\n"+"===")
while True:
    sisestus = (input("> ")).split(" ")
    tähis = str(sisestus[0])
    järjend = sisestus[1:]
    if töötleKäsk(tähis, järjend) == False:
        break