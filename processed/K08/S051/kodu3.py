import film

def töötleKäsk(käsk, järjend):
    if käsk == "K":
        võimalikud_filmid = film.loetleFilmid(järjend[0])
        if võimalikud_filmid == []:
            print("Selles žanris filme pole nimekirjas.")
        else:
            print("Võimalikud filmid on:")
            for el in võimalikud_filmid:
                print(el)
    elif käsk == "L":
        print("Film lisatud!")
        film.lisaFilm(' '.join(järjend[1:]), järjend[0])
    elif käsk == "V":
        film.kustutaFilm(' '.join(järjend))
        print("Film nimekirjast kustutatud!\nHead vaatamist!")        
    elif käsk == "E":
        return False
    return True

print('''
=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===
''')
while True:
    sisend = input("> ").split()    
    if not töötleKäsk(sisend[0], sisend[1:]):
        break