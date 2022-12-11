import film
print("=== FILMIANDMEBAAS === \n Kuva filmid: K <žanr> \n Lisa film:   L <žanr> <film> \n Vaata filmi: V <filmi nimi> \n Lõpeta:      E")

def töötleKäsk(a,b):
    if a[0]=="K":
        b=b.strip("")
        film.loetleFilmid(b)
        return True
    elif a[0] == "L":
        b=b.strip()
        b=b.split(" ")
        v=b[1:]
        v=" ".join(v)
        film.lisaFilm(v,b[0])
        return True
    elif a[0] == "V":
        b=b.strip()
        film.kustutaFilm(b)
        print("Film nimekirjast kustutatud! \n Head vaatamist!")
        return True
    elif a[0]== "E":
        return False
while True:
    n=input("")
    if n=="E":
        break
    a=n[0]
    b=n[2:]
    töötleKäsk(a,b)
        
    