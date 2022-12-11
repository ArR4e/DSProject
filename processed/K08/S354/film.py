def algFilm():
    f = open('filmid.txt')
    r = f.read()
    r = r.strip()
    r = r.split('\n')
    s = []
    for i in range(len(r)):
        a = r[i]
        a = a.split(' - ')
        s += a
    f.close()
    return s

def loetleFilmid(zanr):
    a = algFilm()
    nimed = []
    
    while True:
        try:
            ind = a.index(zanr)
            ind1 = ind - 1
            nimi = a[ind1]
            nimi = nimi.strip()#### ubiraet probel i n
        
            nimed += [nimi]
            del a[ind]
        except:
            break
    
    return nimed



def lisaFilm(a, b):
    rida = algFilm()
    a = ' ' + a
    rida += [a] + [b]
    c = 0
    
    
    x = int(len(rida)/2)
    
    f = open('filmid.txt', 'w')
    for sona in range(x):
        nimi = rida[c]
        c += 1
        zanr = rida[c]
        f.write(' ' + str(nimi). strip() + ' - ' + str(zanr) + '\n')
        c += 1
    f.close()
    
def kustutaFilm(nimi):
    rida = algFilm()
    nimi = ' ' + nimi
    x = int(len(rida)/2)
    c = 0
    f = open('filmid.txt', 'w')
    if nimi in rida:
        for sona in range(x):
            if rida[c] == nimi:
                c += 2
            else:
                
                n = rida[c]
                c += 1
                z = rida[c]
                f.write(' ' + str(n). strip() + ' - ' + str(z) + '\n')
                c += 1
    
    f.close()
    

    
    
    
    