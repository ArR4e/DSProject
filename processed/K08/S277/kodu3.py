import film

print('''=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===''')

def töötleKäsk(tähis, sisestus):
    if len(sisestus) == 1:
        nimi = sisestus[0]
    while True:
        if tähis == 'K':
            print('Võimalikud filmid on:')
            print('\n'.join(film.loetleFilmid(nimi)))
            break
        elif tähis == 'L':
            žanr = sisestus[0]
            sisestus.remove(žanr)
            sisestus = ' '.join(sisestus)
            film.lisaFilm(sisestus, žanr)
            print('Film lisatud!')
            break
        elif tähis == 'V':
            sisestus = ' '.join(sisestus)
            film.kustutaFilm(sisestus)
            print('''Film nimekirjast kustutatud!
Head vaatamist!''')
            break
        elif tähis == 'E':
            return False
        
while True:
    sisestus = (input()).split(' ')
    tähis = sisestus[0]
    sisestus.remove(tähis)
    if töötleKäsk(tähis, sisestus) is False:
        break
    
