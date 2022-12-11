def loetleFilmid(in_zanr):
    fail = open('filmid.txt', 'r', encoding="utf-8")
    loetelu = []
    for rida in fail:
        zanr = rida.rsplit('-', 1)[-1].strip('\n').strip()
        if in_zanr == zanr:
            loetelu.append(rida.rsplit('-', 1)[0].strip())
    fail.close()
    return loetelu

def lisaFilm(nimi, zanr):
    fail = open('filmid.txt', 'a', encoding="utf-8")
    fail.write('\n' + nimi + ' - ' + zanr)
    fail.close()

def kustutaFilm(nimi):
    fail = open('filmid.txt', 'r', encoding="utf-8")
    read = fail.readlines()
    fail.close()
   
    fail = open('filmid.txt', 'w', encoding="utf-8")
    for rida in read:
        if rida.split('-')[0].strip() != nimi:            
            fail.write(rida)
    fail.close()

#print(loetleFilmid('märul'))
#lisaFilm('Borat', 'komöödia')
#kustutaFilm('Shrek')

