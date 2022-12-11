from film import *

def töötleKäsk(käsk,järjend):
    if käsk == 'K':
        for film in loetleFilmid(järjend[0]):
            print(film)
        return True
    if käsk == 'L':
        žanr2 = järjend[0]
        film2 = ' '.join(järjend[1:])
        if žanr2 != '' or film2 != '':
            lisaFilm(film2, žanr2)
        return True
    if käsk == 'V':
        kustutaFilm(järjend[0])
    if käsk == 'E':
        return False

print('''=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===''')
while True:
    try:
        sisend = input('').split()
        if töötleKäsk(sisend[0],sisend[1:]) == False:
            break
    except:
        continue



