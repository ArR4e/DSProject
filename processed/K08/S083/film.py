import re
def loetleFilmid(žanr):
    f = open('filmid.txt', encoding = 'utf-8')
    fail = f.readlines()
    f.close()
    if fail == []:
        return []
    žanrid = []
    filmid= []
    fail = ' '.join(fail)
    fail = re.split(' - |\n',fail)
    
    n=0
    while n<len(fail):
        film = fail[n].strip()
        žanrNimi = fail[n+1].strip()
        filmid.append(film)
        žanrid.append(žanrNimi)
        n+=2
    indeks = [i for i, x in enumerate(žanrid) if x == žanr]
    vastus = [ filmid[i] for i in indeks]
    return vastus

def lisaFilm(nimi, žanr):
    f = open('filmid.txt', 'a', encoding = 'utf-8')
    f.write('\n'+nimi+ ' - '+ žanr)
    f.close()
    
    
    
def kustutaFilm(nimi):
    f = open('filmid.txt', encoding = 'utf-8')
    read = f.readlines()
    f.close()
    f2 = open('filmid.txt', 'w', encoding='utf-8')
    for rida in read:
        if rida[0:len(nimi)] != nimi:
            f2.write(rida)
    f2.close()

