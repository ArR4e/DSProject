import film

def töötleKäsk(sõne, järjend):
    if sõne == "K":
        print("Võimalikud filmid on:")
        for el in film.loetleFilmid(järjend[0]):
            print(el)
    
    if sõne == "L":
        nimi = (" ".join(järjend[1:len(järjend)]))
        zharn = järjend[0]
        film.lisaFilm(nimi, zharn)
        print("Film lisatud!")
        
    if sõne == "V":
        nimi = (" ".join(järjend[0: len(järjend)]))
        film.kustutaFilm(nimi)
        print("Film nimekirjast kustutatud")
        print("Head vaatamist!")
        

print("=== FILMIANDMEBAAS ===")
print("Kuva filmid: K <žanr>")
print("Lisa film:   L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta:      E")
print("===")

while True:
    käsk = str(input()).split(" ")
    töötleKäsk(käsk[0], käsk[1:len(käsk)])
    
    if käsk[0] == "E":
        break
    