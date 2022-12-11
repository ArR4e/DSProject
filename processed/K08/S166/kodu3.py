from film import loetleFilmid
from film import lisaFilm
from film import kustutaFilm
print('=== Filmiandmebaas ===')
print('Kuva filmid: K <žanr>')
print('Lisa film:   L <žanr> <film>')
print('Vaata filmi: V <filmi nimi>')
print('Lõpeta:      E')
print('===')
def töötleKäsk(käsk, järjend):
    if käsk == 'K':
        filmid = loetleFilmid(järjend[1])
        print('Võimalikud filmid on:')
        for el in filmid:
            print(el)
        return True
    elif käsk == 'L':
        lisaFilm(järjend[1],järjend[0])
        print('Film lisatud')
        return True
    elif käsk == 'V':
        kustutaFilm(järjend[0])
        print('Film nimekirjast kustutatud!\nHead vaatamist!')
        return True
    elif käsk == 'E':
        return False
while True:
    sisend=input('> ')
    käsk=sisend[0]
    sisend = sisend.split(' ')
    if käsk == 'K':
        žanr = [sisend[1]]
        nimi = ['pole']
    elif käsk == 'L':
        nimi = [sisend[1]]
        žanr = [' '.join(sisend[2:])]
    elif käsk == 'V':
        žanr = ['pole']
        nimi = [' '.join(sisend[1:])]
    järjend = nimi + žanr
    if töötleKäsk(käsk,järjend) == True:
        continue
    else:
        break
    
