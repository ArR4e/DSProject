import film

print('=== FILMIANDMEBAAS ===' + '\n' + 'Kuva filmid: K <zanr>' + '\n' + 'Lisa film: L <zanr> <film>' + '\n' + 'Vaata filmi: V <filmi nimi>' + '\n' + 'Lõpeta: E')

def töötleKäsk(tähis, järjend):
    if tähis == 'K':
        #1 muutuja loetleFilmidel
        print("Võimalikud filmid on:\n")
        print(film.loetleFilmid(järjend))
    elif tähis == 'L':
        #2 muutujat lisaFilmil
        film.lisaFilm(järjend[0], järjend[1])
        print("Film lisatud!")
    elif tähis == 'V':
        #1 muutuja kustutaFilmil
        print("Film nimekirjast kustutatud!\n Head vaatamist!")
        film.kustutaFilm(järjend)

while True:
    soov = input()
    if soov.startswith('K'):
        sisu = soov.split(' ')
        tähis = sisu[0]
        järjend = sisu[1]
        töötleKäsk(tähis, järjend)
    elif soov.startswith('L'):
        sisu = soov.split(' ')
        if len(sisu) >= 3:
            tähis = sisu[0]
            zanr = sisu[1]
            nimi = soov.split(' ')[2:len(sisu)]
            nimi[2:len(sisu)] = [' '.join(nimi[2:len(sisu)])]
            nimi2 = ''
            for el in nimi:
                nimi2 += el + ' '
            järjend = []
            järjend.append(nimi2.rstrip())
            järjend.append(zanr)
            töötleKäsk(tähis, järjend)
    elif soov.startswith('V'):
        sisu = soov.split(' ')
        if len(sisu) >= 2:
            tähis = sisu[0]
            nimi = soov.split(' ')[1:len(sisu)]
            nimi[1:len(sisu)] = [' '.join(nimi[1:len(sisu)])]
            nimi2 = ''
            for el in nimi:
                nimi2 += el + ' '
            järjend = []
            järjend.append(nimi2.rstrip())
            nimi3 = ''
            for el in järjend:
                nimi3 += el
            töötleKäsk(tähis, nimi3)
    elif soov.startswith('E'):
        break       
