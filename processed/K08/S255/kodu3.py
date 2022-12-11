import film

def töötleKäsk(tahis, jarjend):
    if tahis == 'K':
        a = film.loetleFilmid(jarjend)
        print(f'\nVõimalikud filmid on: ')
        for i in a:
            print(i)
        print('\n')
        return True
    
    if tahis == 'L':
        film.lisaFilm(nimi[1], nimi[0])
        return True
    
    if tahis == 'V':
        film.kustutaFilm(nimi)
        return True
    
    if tahis == 'E':
        return False
    
while True:
    print('Tere tulemast juku filmikataloogi. Alljärgnevad käsud aitavad sul siin programmis navigeerida.' +
    '\nKuva filmid: K <žanr>' +
    '\nLisa film:   L <žanr> <film>' +
    '\nVaata filmi: V <filmi nimi>' +
    '\nLõpeta:      E\n')
    algus = str(input('Kirjuta siia täht, mida soovid teha. Valikuteks on K; L; V; E: '))

    if algus == 'K':
        zanr = (input('Sisesta mis žanri filme sa soovid näha loetelust: ')).split(' ', 1)
        if töötleKäsk(algus, zanr[0]) == True:
            continue
    if algus == 'L':
        print('Sisesta mis žanr ja mis film on.')
        nimi = (input('film: ')).split(' ', 1)
        if töötleKäsk(algus, nimi[0]) == True:
            continue
    if algus == 'V':
        nimi = str(input('Sisesta filmi nimi, mida soovid kustutada.\n Filmi nimi: '))
        if töötleKäsk(algus, nimi) == True:
            continue
    if algus == 'E':
        print('Head aega!')
        break