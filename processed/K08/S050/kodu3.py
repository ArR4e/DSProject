from film import *


def töötleKäsk(käsk, andmed):
    while True:
        if käsk== 'K':
            järjend=loetleFilmid(andmed)
            print('Võimalikud filmid on: ')
            for x in järjend:
                print(x)
            break
        if käsk== 'L':
            zanr,nimi = andmed.split(' ',1)
            lisaFilm(nimi,zanr)
            print('Film lisatud!')
            break
        
        if käsk== 'V':
            kustutaFilm(andmed)
            print('Film nimekirjast kustutatud!')
            print('Head vaatamist!')
            break
        
print('Kuva filmid: K <žanr> \nLisa film:   L <žanr> <film> \nVaata filmi: V <filmi nimi> \nLõpeta:      E ')

s= input()
käsk=s[0]
s= s[1::]
andmed = s.strip()

while True:
    töötleKäsk(käsk, andmed)
    s = input()
    käsk = s[0]
    if käsk == 'E':
        break
    else:
        s = s[1::]
        andmed=s.strip()