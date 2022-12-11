import film

# args - sõnede järjend
def töötleKäsk(käsk, *args):    
    # kui kasutaja ei sisestanud argumente
    if len(args[0]) == 0 and not käsk == "E":
        print("See käsklus nõuab argumente")
        return True
    # kuva žanrile vastavad filmid
    if käsk == "K":
        filmid = film.loetleFilmid(" ".join(args[0]))
        print("Võimalikud filmid on:")
        for f in filmid:
            print(f)
        return True
    # lisa film
    elif käsk == "L":
        film.lisaFilm(" ".join(args[0][1:]), args[0][0])
        print("Film listatud!")
        return True
    # võta film
    elif käsk == "V":
        film.kustutaFilm(" ".join(args[0][:]))
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
        return True
    # välju (tagasta seekord False)
    elif käsk == "E":
        return False
    # kasutaja sisestas midagi muud
    else:
        print("Sobimatu käsklus!")
        return True

print("""
=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===
""")
jätka = True
while jätka:
    # tükelda sisend
    sisend = input("@ ").split()
    # esimeseks argumendiks võta esimene tükk, ülejäänud tükid
    # teiseks argumendiks
    jätka = töötleKäsk(sisend[0].upper(), sisend[1:])
