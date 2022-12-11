from film import*
def töötleKäsk(taht, film):
    taht=kask[:1]
    
    if taht=='E':
        return False
    
    else:
        if taht=='K':
            zanr=kask[2:]
            while loetleFilmid(zanr)==[]:
                print('Sobivaid filme ei leidu, sisestage zanr uuesti:')
                zanr=input()
            print('Võimalikud filmid on: ')
            print(loetleFilmid(zanr))
        
        elif taht=='L':
            zanr=kask[2:kask[2:].find(' ')+2]
            nimi=kask[kask[2:].find(' ')+3:]
            lisaFilm(nimi, zanr)
            print('Film lisatud!')
        
        elif taht=='V':
            nimi=kask[2:]
            kustutaFilm(nimi)
            print('Film nimekirjast kustutatud!')
        return True
taht=''
film=[]
kask=''


while töötleKäsk(taht, film):
    kask=input()