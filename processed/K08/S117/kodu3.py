#alustasin 16.10.2021 (00:24)
import film

def töötleKäsk(kask, argumentid):
    if kask == 'K':
        print('Võimalikud filmid on: ')
        filmid = film.loetleFilmid(argumentid[0])
        if filmid == []:
            print('Pole soovitud žanrist ühtegi filmi! Valige uuesti!')
            return True
        else:
            for i in filmid:
                print(i)
            return True
    if kask == 'L':
        järjend = argumentid
        film.lisaFilm(' '.join(järjend[1:]), järjend[0])
        print('Film lisatud!')
        return True
    if kask == 'V':
        film.kustutaFilm(' '.join(argumentid[0:]))
        print('Film nimekirjast kustutatud!')
        print('Head vaatamist!')
        return True
    if kask == 'E':
        return False

print('=== FILMIANDMEBAAS ===')
print('Kuva filmid: K <žanr>')
print('Lisa film:   L <žanr> <film>')
print('Vaata filmi: V <filmi nimi>')
print('Lõpeta:      E')
print('===')

while True:
    kasutaja = input('> ')
    käsulist = kasutaja.split()
    käsk = käsulist[0]
    argumentid = käsulist[1:]
    check = töötleKäsk(käsk, argumentid)
    print('')
    if check == False:
        break