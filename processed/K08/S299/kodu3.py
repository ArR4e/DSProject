from film import *
while True:
    sisend=str(input('Sisestage käskluse tähis ja filmi nimi, zanr või mõlemad: '))
    sisend_list= list(sisend.split(' '))
    tähis=sisend_list[0]
    ar=sisend_list.pop(0)
    if tähis == 'E':
       break
    else:
        def töötleKäsk(tähis,ar):
            if tähis == 'K':
               print(loetleFilmid(ar[0]))
               return True
            if tähis == 'L':
               lisaFilm(ar[0],ar[1])
               return True
            if tähis == 'V':
               kustutaFilm(ar[0])
               return True
            if tähis == 'E':
               return False
    
# ma ei saa väga ülesandest aru ning ei oska seda õigesti lahendada.