import film
def töötleKäsk(tähis, järjend):
    with open("filmid.txt", "r+", encoding = "UTF-8") as järjend2:
        for el in järjend:
            if "K" in järjend:
                esimene = film.loetleFilmid(järjend[1])
                teine = "\n".join(esimene)
                print(f'Võimalikud filmid on:\n{teine}')
                return True
            elif "L" in järjend:
                esimene = lisaFilm(järjend2)
                teine = esimene.write(tähis)
                print('Film lisatud!')
                return True
            elif "V" in järjend:
                esimene = film.kustutaFilm(järjend2)
                print('Film nimekirjast kustutatud!\nHead Vaatamist!')
                return True
            elif "E" in järjend:
                return False
print('''=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===''')
tähis = input("> ")
järjend = tähis.split(" ")
töötleKäsk(tähis, järjend)
    
        


