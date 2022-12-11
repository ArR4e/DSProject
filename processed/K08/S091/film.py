def loetleFilmid(zanr):
    a = open('filmid.txt', 'r', encoding='UTF-8')
    b = []
    for rida in a:
        nimi, zanr1 = rida.strip('\n').split(' - ')
        if zanr == zanr1:
            b.append(nimi)
    a.close()
    return b
    
def lisaFilm(nimi,zanr):
    a = open('filmid.txt', 'r+')
    b = ' ' + nimi + ' - ' + zanr
    while True:
        if a.readline()!='':
            continue
        else:
            a.write('\n')
            a.write(' ')
            a.write(b)
            break
    a.close()

def kustutaFilm(nimi):
    a = open('filmid.txt', 'r+')
    read = a.readlines()
    a.close()
    b = open('filmid.txt', 'w+')
    for el in read:
        if nimi in el:
            read.remove(el)
    b.writelines(read)
    b.close()
            
