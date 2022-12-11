import film

def töötleKäsk(käsk, argumendid):
    if käsk == 'K':
        žanr = ''.join(argumendid[0])
        filmid = film.loetleFilmid(žanr)
        if filmid != []:
            print('Võimalikud filmid on:')
            for f in filmid:
                print(f)
        else:
            print('Sellist žanri filme failis ei leidu.')
        return True
    elif käsk == 'L':
        žanr = ''.join(argumendid[0])
        faili_nimi = ' '.join(argumendid[1:])
        if film.lisaFilm(faili_nimi, žanr) == True:
            print('Film lisatud!')
        else:
            print('Film juba failis olemas.')
        return True
    elif käsk == 'V':
        faili_nimi = ' '.join(argumendid)
        if film.kustutaFilm(faili_nimi) == True:
            print('Film nimekirjast kustutatud!')
            print('Head vaatamist!')
        else:
            print('Aga sellist filmi failis ei ole.')
        return True
    elif käsk == 'E':
        return False
        
print(' FILMIANDMEBAAS '.ljust(19, '=').rjust(22, '='))
print('Kuva filmid:'.ljust(12), 'K <žanr>')
print('Lisa film:'.ljust(12), 'L <žanr> <film>')
print('Vaata filmi:'.ljust(12),'V <filmi nimi>')
print('Lõpeta:'.ljust(12), 'E')
print('='*3)

while True:
    käsklus = input('> ').strip().split()
    if käsklus == []:
        continue
    argumendid = []
    for k in käsklus:
        if k in ('K', 'L', 'V', 'E'):
            käsk = k
        else:
            argumendid = argumendid + [k]

    if töötleKäsk(käsk, argumendid) == False:
        break
