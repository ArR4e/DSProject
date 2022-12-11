from film import loetleFilmid, lisaFilm, kustutaFilm

def töötleKäsk(tahis, jarjend):
    
    if tahis == 'K':
        print('> K '+jarjend)
        print('Voimalikud filmid on:')
        filmid = loetleFilmid(jarjend)
        for film in filmid:
            print(film)
            
    elif tahis == 'L':
        jarjend = jarjend.split(' ', 1)
        print('> L '+jarjend[0]+' '+jarjend[1])
        lisaFilm(jarjend[1], jarjend[0])
        print('Film lisatud!')
        
    elif tahis == 'V':
        print('> V '+jarjend)
        kustutaFilm(jarjend)
        print('Film nimekirjast kustutatud!')
        
    else:
        return False
    print('\n')

print('''=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===\n
''')

while True:
    kasutajaVastus = input()
    
    if kasutajaVastus == 'E':
        break
    
    kasutajaVastus = kasutajaVastus.split(' ', 1)
    töötleKäsk(kasutajaVastus[0], kasutajaVastus[1])
