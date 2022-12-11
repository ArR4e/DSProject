from film import *

print('=== FILMIANDMEBAAS ===')
# uus = loetleFilmid(input("Sisesta filmi žanr: "))
# print(uus)

def töötleKäsk(täht, käsk):
    if täht == 'K':
        print('Selle žanri filmid on: ')
        uus = loetleFilmid(käsk)
        a = uus[0]
        b = uus[1]
        print(a + '\n' + b)
        return True
    elif täht == 'L':
        lisa = lisaFilm(käsk[0], käsk[1])
        print('Film lisatud!')
        return True
    elif täht == 'V':
        eemalda = kustutaFilm(käsk)
        print('Film nimekirjast kustutaud!')
        print('Head vaatamist!')
        return True
    else:
        return False
    
töö = ''
While töö == True:
    käsk = input('Sisestage käsklus: ')
    käsk = käsk.split()
    täht = käsk[0].upper()
    if täht == 'K':
        töö = töötleKäsk(täht, käsk[1])
    elif täht == 'L':
        töö = töötleKäsk(täht, käsk[1:])
    elif täht == 'V':
        töö = töötleKäsk(täht, käsk[1])
    elif täht == 'E':
        töö = töötleKäsk(täht, '')
    else:
        print('Antud kasklust ei ole!')
        continue