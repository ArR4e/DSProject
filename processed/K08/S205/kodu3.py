from film import *

def töötleKäsk(tähis, sõne=''):
    if tähis=='E':
        return False
    elif tähis=='K':
        print('Võimalikud filmid on: ')
        try:
            for el in loetleFilmid(sõne):
                print(el)
        except:
            print('Sellest žanrist filme pole nimekirjas')
        return True
    elif tähis=='L':
        a = sõne.replace(' ',' - ',1)
        b=a.split(' - ')
        lisaFilm(b[1],b[0])
        print('Film lisatud!')
        return True
    elif tähis=='V':
        kustutaFilm(sõne)
        print('Film nimekirjast kustutatud!')
        print('Head vaatamist!')
        return True

print('=== FILMIANDMEBAAS ===')
print('Kuva filmid: K <žanr>')
print('Lisa film:   L <žanr> <film>')
print('Vaata filmi: V <filmi nimi>')
print('Lõpeta:      E')
print('===')

käsud=[]

while True:
    sisend = str(input(''))
    käsud=sisend.split('\n')
    for el in käsud:
        if el=='E':
            käsud = 'E'
            break
        else:
            töötleKäsk(el[0],el[2:])
    if käsud == 'E':
        break
        
    
    
    
        
