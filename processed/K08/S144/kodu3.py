from film import *
print('=== FILMIANDMEBAAS ===\nKuva filmid: K <žanr>\nLisa film:   L <žanr> <film>\nVaata filmi: V <filmi nimi>\nLõpeta:      E\n===')

def töötleKäsk(a,b):
    if a == 'K':
        print('Võimalikud filmid on:')
        filmid = loetleFilmid(b[0])
        for i in filmid:
            print(i)
    elif a == 'L':
        lisaFilm(b[1],b[0])
        print('Film lisatud!')
    elif a == 'V':
        kustutaFilm(b[0])
        print('Film nimekirjast kustutatud.\nHead vaatamist!')
    else:
        return False
while True:
    sisend = input()
    b = sisend.split()
    b = b[1:]
    if len(b) > 2:
        b[1:] = [' '.join(b[1:])]
    a = sisend[0]
    if töötleKäsk(a,b) == False:
        break