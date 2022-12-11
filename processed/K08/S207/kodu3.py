from film import *

def töötleKäsk(käsklus, info=[]):
    if käsklus == "K":
        print("Võimalikud filmid on:")
        for rida in loetleFilmid(info[0]):
            print(rida)
            
    elif käsklus == "L":
        lisaFilm(" ".join(info[1:]), info[0])
        print("Film lisatud!")
        
    elif käsklus == "V":
        kustutaFilm(" ".join(info))
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
    
    elif käsklus == "E":
        return False
    
    else:
        print("Sisestatud käsklust ei leitud!")
    
    return True

print(f"""=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===""")

while True:
    sisestus = input().split()
    if not töötleKäsk(sisestus[0], sisestus[1:]):
        break
        
        