from film import *

def töötleKäsk(käsk1, käsk2):
    if täht == 'K':
        print('Võimalikud filmid on: ')
        for film in loetleFilmid(käsk1):
            print(film)
        return True
    elif täht == 'L':
        nimi = ''
        for sõna in käsk2:
            nimi += sõna + ' '
        lisaFilm(nimi, käsk1)
        print('Film lisatud!')
        return True
    elif täht == 'V':
        nimi = ''
        for sõna in käsk1:
            nimi += sõna + ' '
        kustutaFilm(nimi)
        print('Film on nimekirjast kustutatud! \n' +
        'Head vaatamist!')
        return True
    elif täht == 'E':
        return False
    
print('\033[3;34m===' + '\033[3;37m FILMIANDMEBAAS ' + '\033[3;34m=== \n' +
      '\033[3;37m' +
      'Kuva filmid: K <žanr> \n' + 
      'Lisa film:   L <žanr> <film> \n' +
      'Vaata filmi: V <filmi nimi> \n' +
      'Lõpeta:      E \n' +
      '\033[3;34m=== \n')

käsk = ''
täht = ''
a = ''
while a != False:
    käsk = input('\033[3;37m> ')
    käsk = käsk.split()
    täht = käsk[0].upper()
    if täht == 'K':
        a = töötleKäsk(käsk[1], '')
    elif täht == 'L':
        a = töötleKäsk(käsk[1], käsk[2:])
    elif täht == 'V':
        a = töötleKäsk(käsk[1:], '')
    elif täht == 'E':
        a = töötleKäsk('','')
    else:
        print('Kasutage ette antud formaate!')
        continue