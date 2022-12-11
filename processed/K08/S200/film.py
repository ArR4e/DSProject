def loetleFilmid(žanr):
    f = open('filmid.txt',encoding='UTF-8')
    kokku_filmid = []
    tüüp = []
    nimekiri = []
    for rida in f:
        andmed = rida.strip().split(' - ')
        kokku_filmid.append(andmed[0])
        tüüp.append(andmed[1])
    i = 0
    while i < len(tüüp):
        if tüüp[i] == žanr:
            nimekiri.append(kokku_filmid[i])
            i += 1
        else:
            i += 1
    f.close()
    
    return nimekiri
        

def lisaFilm(nimi,žanr):
    f = open('filmid.txt','a')
    f.write('\n' + nimi + ' - ' + žanr)
    f.close()

def kustutaFilm(nimi):
    f = open('filmid.txt',encoding='UTF-8')
    uus = []
    for rida in f:
        if nimi not in rida:
            uus.append(rida)
    f.close()
    f = open('filmid.txt','w')
    for el in uus:
        f.write(el)
    f.close()
