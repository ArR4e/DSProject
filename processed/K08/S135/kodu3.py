from film import *

def töötleKäsk(käsk, argumendid):
    if argumendid == [] and käsk != 'E':
        return True
    if käsk == 'K':
        print('Võimalikud filmid on: ')
        for film in loetleFilmid(argumendid[0]):
            print(film)
    elif käsk == 'L':
        lisaFilm(argumendid[1], argumendid[0])
        print('Film lisatud!')
    elif käsk == 'V':
        kustutaFilm((argumendid[0] + ' ' + argumendid[1]).strip())
        print('Film nimekirjast kustutatud!\nHead vaatamist!')
    elif käsk == 'E':
        return False
    return True

print('''=== FILMIANDMEBAAS ===\n
        Kuva filmid: K <žanr>\n
        Lisa film:   L <žanr> <film>\n
        Vaata filmi: V <filmi nimi>\n
        Lõpeta:      E\n
        ===''')

isContinuing = False
while True:
    sisend = input().split()
    if sisend == []:
        continue
    elif sisend == ['E']:
        isContinuing = töötleKäsk(sisend[0], [])
    else:
        isContinuing = töötleKäsk(sisend[0], [sisend[1], ' '.join(sisend[2:])])
    
    if not isContinuing:
        break
        


