import film

def töötleKäsk(kask, args):
    if kask == 'K':
        filmid = film.loetleFilmid(args[0])
        if len(filmid) == 0:
            print('Soovitud žanrist pole ühtegi filmi.')
        else:
            print('Võimalikud filmid on:')
            print('\n'.join(filmid))
        return True
    elif kask == 'L':
        film.lisaFilm(' '.join(args[1:]), args[0])
        print('Film lisatud!')
        return True
    elif kask == 'V':
        film.kustutaFilm(' '.join(args))
        print('Film nimekirjast kustutatud!')
        print('Head vaatamist!')
        return True
    elif kask == 'E':
        return False
    else:
        print('Sisestati vigane käsk: ' + kask)
        return True

print("""
=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===
""")

jatka = True
while jatka:
    sisend = input('> ').split(' ')
    #print(sisend)
    jatka = töötleKäsk(sisend[0], sisend[1:])