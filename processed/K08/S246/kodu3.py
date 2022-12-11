import film
def töötleKäsk():
    print('===', 'FILMIANDMEBAAS', '===')
    print('Kuva filmid:'.ljust(15), 'K <žanr>')
    print('Lisa film:'.ljust(15), 'L <žanr> <filmi nimi>')
    print('Vaata filmi:'.ljust(15), 'V <filmi nimi>')
    print('Lõpeta:'.ljust(15), 'E')
    print('===')
    while True:
        käsk = input()
        try:
            list(käsk)
            if käsk[0] == 'E':
                break
            elif käsk[0] == 'K':
                käsk = käsk[2:]
                žanr = ''.join(käsk)
                nimekiri = film.loetleFilmid(žanr)
                if nimekiri == []:
                    print('Selles žanris hetkel filme ei ole.')
                else:
                    print('Võimalikud filmid on:')
                    for filminimi in nimekiri:
                        print(filminimi)
            elif käsk[0] == 'L':
                käsk = käsk[2:]
                nimekiri = ''.join(käsk).split(' ')
                žanr = nimekiri[0]
                filminimi = nimekiri[1:]
                nimi = ' '.join(filminimi)
                film.lisaFilm(nimi, žanr)
                print('Film lisatud!')
            elif käsk[0] == 'V':
                käsk = käsk[2:]
                filminimi = ''.join(käsk)
                film.kustutaFilm(filminimi)
                print('Film nimekirjast kustutatud!\nHead vaatamist!')
        except:
            print('Sellist käsku ei leitud.')

töötleKäsk()