'''
Funktsioon loetleFilmid, mis võtab argumendiks žanri nime ning tagastab järjendi kõikide filmide nimedega, mis on etteantud žanrist.
Funktsioon lisaFilm, millel on kaks argumenti. Esimeseks argumendiks on nimi ning teiseks žanr. Funktsioon peab olemasolevasse faili filmid.txt soovitud filmi koos žanriga lisama kujul nimi - žanr, näiteks Spider-Man - märul.
Funktsioon kustutaFilm, mis võtab argumendiks filmi nime ning kustutab selle olemasolevast tekstifailist ära.
'''

def loetleFilmid(genre):
    nimekiri = []
    f = open('filmid.txt', 'r+', encoding = 'UTF-8')
    x = []
    for a in f:
        x.append(a.strip())
        if genre in a:
            n = a.split(' - ')
            nimekiri.append(n[0])
    return nimekiri
     
def lisaFilm(nimi, genre):
    f = open('filmid.txt', 'r+', encoding = 'UTF-8')
    x = []
    for a in f:
        x.append(a.strip())
    x.append(nimi + ' - '+ genre)
    f.write(nimi + ' - '+ genre + '\n')
    #print('peale filmi lisamist: ' + str(x))
    f.close()
    
def kustutaFilm(nimi):
    f = open('filmid.txt', 'r+', encoding = 'UTF-8')
    x = []
    for a in f:
        x.append(a.strip())
    for l in x:
        if nimi in l:
            x.remove(l)
    #print('kõige viimane kustutamine: ' + str(x))
    f = open('filmid.txt').close()
    f = open('filmid.txt', 'w')
    for n in x:
        f.write(n + '\n')
    f.close()


