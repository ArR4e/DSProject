from film import *

def töötleKäsk(käsk, jär):
    if käsk == 'E':
        return False
    elif käsk == 'K':
        print('Võimalikud filmid on: ')
        for el in loetleFilmid(jär[0]):
            print(el)
        return True
    elif käsk == 'V':
        kustutaFilm(' '.join(jär))
        print('Film nimekirjast kustutatud!')
        print('Head vaatamist!')
        return True
    elif käsk == 'L':
        nimi = ' '.join(jär[1:])
        zanr = jär[0]
        lisaFilm(nimi, zanr)
        print('Film lisatud!')
        return True
    else:
        return False
    
print('Kuva filmid: K <žanr>')
print('Lisa film:   L <žanr> <film>')
print('Vaata filmi: V <filmi nimi>')
print('Lõpeta:      E')

while True:
    sisend = input()
    i = sisend.find(' ')
    sõne = sisend[:i].strip()
    järjend = sisend[i+1:].split()
    if sisend == 'E':
        break
    töötleKäsk(sõne, järjend)