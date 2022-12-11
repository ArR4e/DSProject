from film import *
def töötleKäsk(käsk, argumendid):
    if käsk == 'K':
        filmid = loetleFilmid(argumendid[0])
        while filmid == []:
            print('Sellisest žanrist filme pole.')
            uus_žanr = input('Siestage uus žanr: ')
            filmid = loetleFilmid(uus_žanr)     
        filmid = '\n'.join(filmid)
        print(f'Võimalikud filmid on: \n{filmid}')
        return True
    elif käsk == 'L':
        lisaFilm(' '.join(argumendid[1:]), argumendid[0])
        print('Film lisatud!')
        return True
    elif käsk == 'V':
        kustutaFilm(' '.join(argumendid[0:]))
        print('Film nimekirjast kustutatud!')
        return True
    elif käsk =='E':
        return False
while True:
    sisend = input()
    sisend = sisend.split()
    käsk = sisend[0]
    argumendid = sisend[1:]
    if töötleKäsk(käsk, argumendid) == False:
        break