# 2. Filmide nimekiri / RP

fail = open("filmid.txt", encoding="UTF-8")
nimed = []
zanrid = []
sisu = []

for rida in fail:
    sisu.append(rida.strip())
    rida = rida.split(" - ")
    nimed.append(rida[0].strip())
    zanrid.append(rida[1].strip())
fail.close()
    
def loetleFilmid(z):
    n = 0
    filmid = []
    for el in zanrid:
        if el == z:
            filmid.append(nimed[n])
        n += 1
    return filmid
    
def lisaFilm(n,z):
    nimed.append(n)
    zanrid.append(z)
    sisu.append(n + " - " + z)
    fail = open("filmid.txt",  'a',encoding = "UTF-8")
    fail.write("\n" + n + " - " + z)
    fail.close()   
    
def kustutaFilm(n):
    global uus
    global indeks
    global lols
    fail = open("filmid.txt", 'w', encoding = "UTF-8")
    e = 0
    i = 0
    
    for rida in nimed:
        if rida == n:
            indeks = e
        e += 1
    
    try:
        nimed.remove(n)
        lols = zanrid[indeks]
        zanrid.remove(zanrid[indeks])
    except:
        print("Vale sisend")
        
    try:
        if indeks == len(sisu) - 1:
            uus = indeks - 1
        for rida in sisu:
            if i != indeks:
                try:
                    if uus == i:
                        fail.write(rida)
                    elif i != len(sisu) - 1:
                        fail.write(rida + "\n")
                    else:
                        fail.write(rida)
                except:
                    if i != len(sisu) - 1:
                        fail.write(rida + "\n")
                    else:
                        fail.write(rida)
            i += 1
    except:
        if indeks == len(sisu) - 1:
            uus = indeks - 1
        for rida in sisu:
            if i != len(sisu) + 1:
                try:
                    if uus == i:
                        fail.write(rida)
                    elif i != len(sisu) - 1:
                        fail.write(rida + "\n")
                    else:
                        fail.write(rida)
                except:
                    if i != len(sisu) - 1:
                        fail.write(rida + "\n")
                    else:
                        fail.write(rida)
            i += 1
    
    sisu.remove(n + " - " + lols)
    
    fail.close()
