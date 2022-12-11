from film import *

def töötleKäsk(käsk, argumendid):
    if käsk == "K":
        if argumendid:
            filmid = loetleFilmid(argumendid[0])
            if filmid:
                for film in filmid:
                    print(film)
            else:
                print("Selles žanris filme pole nimekirjas.")
    elif käsk == "L":
        lisaFilm(" ".join(argumendid[1:]), argumendid[0])
        print("Film lisatud!")
    elif käsk == "V":
        kustutaFilm(" ".join(argumendid))
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
    elif käsk == "E":
        return False
        
    return True

print("=== FILMIANDMEBAAS ===")
print("Kuva filmid: K <žanr>")
print("Lisa film:   L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta:      E")
print("===")

jätka = True

while jätka:
    sisend = input("> ").split(" ")
    jätka = töötleKäsk(sisend[0], sisend[1:])
    