import film

def töötleKäsk(kask, arr):
    if kask == "K":
        if film.loetleFilmid(arr[0]) != []:
            print(str(film.loetleFilmid(arr[0])))
        else:
            print('Filme Pole')
    elif kask == "L":
        film.lisaFilm(arr[1], arr[0])
        print('Lisatud!')
    elif kask == "V":
        film.kustutaFilm(' '.join(arr))
        print('Kustutatud')
    elif kask == "E":
        return False
    else:
        print('Tundmatu Käsk')
    return True

while True:
    sisend = input(' ')
    if not töötleKäsk(sisend.split(' ', 2)[0], sisend.split(' ', 2)[1:]):
        break