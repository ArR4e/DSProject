from film import *

def töötleKäsk(n, ls):
    if n == "K":
        film = ls[0]
        filmid = loetleFilmid(film)
        if filmid == []:
            print("Sellisest žanrist filme failis ei ole.")
            return True
        print("Võimalikud filmid:")
        for i in filmid:
            print(i)
        return True
        
    elif n == "L":
        z = ls[0]
        film = " ".join(ls[1:])
        if film == "":
            print("Lisage ka filmi nimi.")
            return True
        lisaFilm(film, z)
        print("Film lisatud!")
        return True
        
    elif n == "V":
        film = " ".join(ls[0:])
        kustutaFilm(film)
        return True
        
    elif n == "E":
        return False
    
    else:
        print("Sellist tegevust ei leitud ("+ n + ") ei leitud. Sisestage uuesti: ")
        return True
    
print("""=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
======================""")
v = True

while v:
    sisend = input("> ")
    sisend = sisend.split(" ")
    k = sisend[0].upper()
    a = sisend[1:]
    v = töötleKäsk(k, a)
