from film import *

def töötleKäsk(tähis, argumendid):
    if tähis == 'K':
        i = 0
        vastus1 = loetleFilmid(argumendid)
        if vastus1 == []:
            return False
        print('\nVõimalikud filmid on: ')
        while i < len(vastus1):
            print(vastus1[i])
            i += 1
        return True
    elif tähis == 'L':
        lisaFilm(uuslist2[1], uuslist2[0])
        return True
    elif tähis == 'V':
        kustutaFilm(argumendid)
        return True
    elif tähis == 'E':
        return False
    return None

uuslist1 = []
uuslist2 = []
uuslist3 = []
x = 2
y = 1

while True:
    kasutaja_sisestus = input('')
    if kasutaja_sisestus[0] == 'K':
        väärtused1 = kasutaja_sisestus.split()
        while töötleKäsk(väärtused1[0], väärtused1[1]) == False:
            print('\nTekstifailis pole soovitud žanrist ühtegi filmi.\nValige mõni muu žanr.')
            väärtused1 = input('\nKuva filmid: ').split()
        continue
    elif kasutaja_sisestus[0] == 'L':
        väärtused2 = kasutaja_sisestus.split()
        while x < len(väärtused2):
            uuslist1.append(väärtused2[x])
            x += 1
        uuslist2.append(väärtused2[1])
        uuslist2.append(' '.join(uuslist1))
        print('\nFilm lisatud!')
        print()
        print(töötleKäsk(väärtused2[0], uuslist2))
        uuslist1 = []
        uuslist2 = []
        x = 2
        continue
    elif kasutaja_sisestus[0] == 'V':
        väärtused3 = kasutaja_sisestus.split()
        while y < len(väärtused3):
            uuslist3.append(väärtused3[y])
            y += 1
        print('\nFilm nimekirjast kustutatud!')
        print('Head vaatamist!')
        print()
        print(töötleKäsk(väärtused3[0], ' '.join(uuslist3)))
        uuslist3 = []
        y = 1
        continue
    elif kasutaja_sisestus[0] == 'E':
        break