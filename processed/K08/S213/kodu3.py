from film import *

def töötleKäsk(tahis, jarjend):
    
    if tahis == "K":
        return loetleFilmid(jarjend[0])
    elif tahis == "L":
        lisaFilm(jarjend[0], jarjend[1])
    elif tahis == "V":
        kustutaFilm(jarjend[0])

print("=== FILMIANDMEBAAS ===")
print("Kuva filmid: K <žanr>")
print("Lisa film:   L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta:      E")
print("===")
print("")

kask = input()

while(True):
    
    if kask[0:1] == "K":
        jarjend = []
        jarjend.append(kask[2: len(kask)])
        filmid = töötleKäsk("K", jarjend)
        print("Võimalikud filmid on:")
        for film in filmid:
            print(film)
            
    elif kask[0:1] == "L":
        jarjend = []
        tyhik = kask.find(" ", 2)
        zanr = kask[2: tyhik]
        nimi = kask[tyhik + 1: len(kask)]
        jarjend.append(nimi)
        jarjend.append(zanr)
        töötleKäsk("L", jarjend)
        print("Film lisatud!")

    elif kask[0:1] == "V":
        jarjend = []
        jarjend.append(kask[2: len(kask)])
        töötleKäsk("V", jarjend)
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
        
    elif kask[0:1] == "E":
        break
    
    print("")
    
    kask = input()