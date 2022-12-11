from film import *
    
def töötleKäsk(kask, argumendid):
    while True:
        if kask == 'K':
            a = loetleFilmid(argumendid)
            print('Võimalikud filmid on : ')
            for el in a:
                print(el)
            return True
        if kask == 'L':
            zanr, nimi = argumendid.split(' ',1)
            lisaFilm(nimi, zanr)
            print('Film lisatud!')
            return True
        if kask == 'V':
            kustutaFilm(argumendid)
            print('Film nimekirjast kustutatud!', 'Head vaatamist!', sep=('\n'))
            return True
        if kask == 'E':
            return False
        
print("Kuva filmid: K <zanr> \nLisa film:   L <zanr> <filmi nimi> \nVaata filmi: V <filmi nimi> \nLõpeta:      E ")

sisend = input()
kask = sisend[0]
sisend = sisend[1::]
argumendid = sisend.strip()

while True:
    töötleKäsk(kask, argumendid)
    sisend = input()
    kask = sisend[0]
    if kask == 'E':
        break
    else:
        sisend = sisend[1::]
        argumendid = sisend.strip()
    
