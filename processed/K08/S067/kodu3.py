import film
def töötleKäsk(käsk, argumendid):
    if käsk == 'K':
        print('võimalikud filmid on:')
        filmid = film.loetleFilmid(argumendid[0])
        for i in filmid:
            print(i)
        return True

    if käsk == 'L':
        film.lisaFilm(argumendid[1], argumendid[0])
        print('Film lisatud!')
        return True
    if käsk == 'V':
        film.kustutaFilm(' '.join(argumendid))
        print('Film nimekirjast kustutatud!' + '\n' + 'Head vaatamist!')
        return True

    if käsk == 'E':
        return False

while True:
    x = input('Sisesta käsk:')
    y = x.split(' ', 2)
    if töötleKäsk(y[0], y[1:len(y)]):
        continue
    else:
        break