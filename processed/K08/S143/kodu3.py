from film import *

def töötleKäsk(t,l):
    if t == "K":
        print("Võimalikud filmid on:")
        print('\n'.join(loetleFilmid(l[:l.find(" ")])))
        return True
    elif t == "L":
        print("Film lisatud!")
        lisaFilm(l[l.find(" ")+1:],l[:l.find(" ")])
        return True
    elif t == "V":
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
        kustutaFilm(l)
        return True
    elif t == "E":
        return False
print("=== FILMIANDMEBAAS ===\nKuva filmid: K <žanr>\nLisa film:   L <žanr> <film>\nVaata filmi: V <filmi nimi>\nLõpeta:      E")
while (lambda x: töötleKäsk(x[:x.find(" ")],x[x.find(" ")+1:]))(input()):
    pass