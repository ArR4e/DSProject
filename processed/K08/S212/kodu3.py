from film import *

def töötleKäsk(tahis,jarjend):
    if tahis == 'K':
        filmid = loetleFilmid(jarjend[0])
        print("Võimalikud filmid on:")
        for film in filmid:
            print(film)
        return True
    if tahis == 'L':
        lisaFilm(jarjend[1],jarjend[0])
        print("Film lisatud!")
        return True
    if tahis == 'V':
        kustutaFilm(jarjend[0])
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
        return True
    if tahis == 'E':
        return False

i = True
print("""=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===""")
while i:
    sis = ''
    sis = input()
    inputsplit = sis.split()
    key = sis[0]
    if key=='K' or key=='V':
       töötleKäsk(key, [sis[2:len(sis)]])
    elif key=='L':
        i = 0
        film = ''
        for inp in inputsplit:
            if i > 1:
                film += inp + ' '
            i+=1
        töötleKäsk(key,[inputsplit[1], film.rstrip()])
    elif key == 'E':
         i = töötleKäsk(key,[])
    print("")
    