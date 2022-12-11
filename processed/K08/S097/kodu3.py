#Kuva filmid: K <žanr>
#Lisa film:   L <žanr> <film>
#Vaata filmi: V <filmi nimi>
#Lõpeta:      E

import film

def funktsioonKäsk(käsuTähis, käsuArgument):
    while True:
        if käsuTähis == "K":
            print("Võimalikud filmid on:\n" + "\n".join(film.loetleFilmid(" ".join(käsuArgument))))
            käsuTähis = input("Sisesta käsk: ")
            käsuArgument = list(input("Sisesta argument: ").split()) 
            continue
        elif käsuTähis == "L":
            žanr = käsuArgument[0]
            nimi = " ".join(käsuArgument[1:])
            film.lisaFilm(nimi, žanr)
            print("Film lisatud!")
            käsuTähis = input("Sisesta käsk: ")
            käsuArgument = list(input("Sisesta argument: ").split())
            continue
        elif käsuTähis == "V":
            film.kustutaFilm(" ".join(käsuArgument))
            print("Head vaatamist! Film nimekirjast kustutatud.")
            käsuTähis = input("Sisesta käsk: ")
            käsuArgument = list(input("Sisesta argument: ").split())
            continue
        elif käsuTähis == "E":
            break
        
A = input("Sisesta käsk: ")
B = list(input("Sisesta argument: ").split()) 
        
funktsioonKäsk(A, B)
