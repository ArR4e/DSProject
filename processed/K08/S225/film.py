def loetleFilmid(a):
    f = open('filmid.txt', encoding = 'UTF-8')
    järg = []
    zanr = []
    vilm = []
    žanr = []
    film = []
    väljund = []

    for rida in f:
        rida = rida.replace('\n','').split(' - ')
        for sõna in rida:
            järg.append(sõna)
        
    for nr in range(len(järg)):
        if nr % 2:
            zanr.append(nr)
        else:
            vilm.append(nr)  

    for n in zanr:
        p = järg[n]
        žanr.append(p)
    for m in vilm:
        q = järg[m]
        film.append(q)
        
    for i in range(len(žanr)):
        if žanr[i] == a:
            s = film[i].strip()
            #strip() - eemaldab tühikud sõne eest ja tagant nt ' kool ' -> 'kool'
            väljund.append(s)
        else:
            continue
    f.close()
    return väljund
    
def lisaFilm(nimi, zanr):
    f = open('filmid.txt','r+', encoding = 'UTF-8')
    read = f.readlines()
    nimi = nimi.strip()
    if read != []:
        f.write('\n ' + nimi + ' - ' + zanr)
    else:
        f.write(nimi + ' - ' + zanr)
    f.close()
    
def kustutaFilm(nimi):
    nimi = nimi.strip()
    with open('filmid.txt', encoding = 'UTF-8') as f:
        read = f.readlines()

    with open('filmid.txt', 'w') as f:
        for i in read:
            i = i.replace('\n','').split(' - ')
            a = i[0].strip()
            if a != nimi:
                f.write(i[0] + ' - ' + i[1] + '\n')           
    f.close()