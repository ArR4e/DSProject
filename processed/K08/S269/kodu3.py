import film
def töötleKäsk(k, l):
    if k == "E":
        return False
    elif k == "K":
        print("Võimalikud filmid on:")
        print(*film.loetleFilmid(l[0]), sep="\n")
        return True
    elif k == "L":
        film.lisaFilm(l[1], l[0])
        print("Film lisatud!")
        return True
    elif k == "V":
        film.kustutaFilm(l[0])
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
        return True
    else:
        return True
print("=== FILMIANDMEBAAS === \nKuva filmid: K <žanr>\nLisa film:   L <žanr> <film>\nVaata filmi: V <filmi nimi>\nLõpeta:      E\n===")
a = True
while a:
    sis = input("")
    if sis == "":
        continue
    elif sis[0] == "V":
        a = töötleKäsk("V", sis.split(" ", 1)[1:])
    elif sis[0] == "L":
        a = töötleKäsk("L", sis.split(" ", 2)[1:])
    else:
        a = töötleKäsk(sis.split()[0], sis.split(" ", 1)[1:])
    
        
