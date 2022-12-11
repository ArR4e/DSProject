import film

def töötleKäsk(käsk, järjend=None):
    if käsk == 'K':
        zanr = järjend[0]
        filmid = film.loetleFilmid(zanr)
        print('Võimalikud filmid on: ' + '\n' + '\n'.join(filmid)) 
        return True
    elif käsk == 'L':
        nimi = järjend[0]
        zanr = järjend[1]
        film.lisaFilm(nimi, zanr)
        print('Film lisatud!')
        return True
    elif käsk == 'V':
        nimi = järjend[0]
        film.kustutaFilm(nimi)
        print('Film nimekirjast kustutatud!\nHead vaatamist!')
        return True
    else:
        return False
    
    
while True:    
    sisendisõne = input()
    sisendijärjend = sisendisõne.split(' ')
    käsk = sisendijärjend[0]
    if käsk == 'V':
        filmjärjend = sisendijärjend[1:]
        järjend = [' '.join(filmjärjend)]
        töötleKäsk(käsk,järjend)
    elif käsk == 'K':
        zanrjärjend = sisendijärjend[1]
        järjend = [zanrjärjend]
        töötleKäsk(käsk,järjend)
    elif käsk == 'L':               
        zanrjärjend = sisendijärjend[1]
        filmjärjend = sisendijärjend[2:]
        järjend = [' '.join(filmjärjend), zanrjärjend]
        töötleKäsk(käsk,järjend)
    else:
        töötleKäsk(käsk)
        break