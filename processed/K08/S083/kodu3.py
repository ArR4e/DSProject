from film import *

def töötleKäsk(tähis, järjend):
    if tähis == 'K':
        vastus1 = loetleFilmid(*järjend)
        n=0
        while n<len(vastus1):
            print(vastus1[n])
            n+=1
        print()
        if vastus1 != []:
            return True
        else:
            return False
    elif tähis == 'L':
        lisaFilm(järjend[1], järjend[0])
        return True
    elif tähis == 'V':
        kustutaFilm(*järjend)
        return True
    elif tähis == 'E':
        return False
    
print('=== FILMIANDMEBAAS ===')

uuslist1=[]
uuslist2=[]
x=2

while True:
    sisend = input('')
    if sisend[0] == 'K':
        print('Võimalikud filmid on:')
        i=sisend.find(' ')
        käsk=sisend[:i].strip()
        järjend=sisend[i+1:].split()
        if töötleKäsk(käsk, järjend) == False:
            print('Sellise žanriga filme pole')
            continue
        else:
            continue
    elif sisend[0] == 'L':
        väärtused2 = sisend.split()
        while x < len(väärtused2):
            uuslist1.append(väärtused2[x])
            x+=1
        uuslist2.append(väärtused2[1])
        uuslist2.append(' '.join(uuslist1))
        print('Film lisatud!')
        töötleKäsk(väärtused2[0], uuslist2)
        uuslist1 = []
        uuslist2 = []
        x = 2
        continue
    elif sisend[0] == 'V':
        print('Film nimekirjast kustutatud!\n'
              'Head vaatamist!')
        i=sisend.find(' ')
        käsk=sisend[:i].strip()
        järjend=sisend[i+1:].split()
        järjend=[' '.join(järjend)]
        töötleKäsk(käsk, järjend)
        continue
    elif sisend[0] == 'E':
        töötleKäsk(sisend, [])
        break