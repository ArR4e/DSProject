import film

def töötleKäsk(kask, argumentid):
    if kask == 'K':
        print('Võimalikud filmid on:')
        for kino in film.loetleFilmid(argumentid[0]):
            print(kino)
    elif kask == 'L':
        film.lisaFilm(argumentid[1], argumentid[0])
        print('Film lisatud!')
    elif kask == 'V':
        film.kustutaFilm(argumentid[0])
        print('Film nimekirjast kustutatud!')
        print('Head vaatamist!')
    elif kask == 'E':
        return False
    return True


print("""
=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===
""")
while True:
    kasutaja_sisend = input('> ')
    
    kask = kasutaja_sisend[0]
    if kask == 'L':
        eraldaja = kasutaja_sisend[2:].find(' ') + 2
        argumentid = [kasutaja_sisend[2:eraldaja]] + [kasutaja_sisend[eraldaja+1:]]
    else:
        argumentid = [kasutaja_sisend[2:]]
    
    if not töötleKäsk(kask, argumentid): break
 
