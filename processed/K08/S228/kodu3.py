from film import *

def töötleKäsk(käsk, järjend):
    if käsk == 'K':
        if loetleFilmid(järjend) != []:
            print('Võimalikud filmid on:')
            loetleFilmid(järjend)
            for el in loetleFilmid(järjend):
                print(el)
        else:
            print('Antud kategoorias pole ühtegi filmi. Proovi uuesti.')
        return True
    elif käsk == 'L':
        järjend_spl= järjend.split(' ', 1)
        žanr_ = järjend_spl[0]
        nimi_ = ' '.join(järjend_spl[1:])
        lisaFilm(nimi_, žanr_)
        print('Film lisatud!')
        return True
    elif käsk == 'V':
        kustutaFilm(järjend)
        print('Film nimekirjast kustutatud!')
        print('Head vaatamist!')
        return True
    elif käsk == 'E':
        return False

print('Kuva filmid: K <žanr>')
print('Lisa film:   L <žanr> <film>')
print('Vaata filmi: V <filmi nimi>')
print('Lõpeta:      E')

while True:
    tulemus = input('')
    if töötleKäsk(tulemus[0], tulemus[2:]) == False:
        break