def loetleFilmid(zanr):
    file = open("filmid.txt","r",encoding="UTF-8")
    data = file.readlines()
    file.close()
    nimed = []
    zanrid = []
    filmid = []
    for i in range(len(data)):
        nimed.append(data[i][:data[i].index(" - ")].strip())
        zanrid.append(data[i][data[i].index(" - ")+2:].strip())
    nimed_temp = nimed
    zanrid_temp = zanrid
    mitu = zanrid.count(zanr)
    for i in range(mitu):
        filmid.append(nimed_temp[zanrid_temp.index(zanr)])
        del zanrid_temp[zanrid_temp.index(zanr)]
        del nimed_temp[nimed_temp.index(filmid[i])]
    return filmid

def lisaFilm(nimi,zanr):
    file = open("filmid.txt","a",encoding="UTF-8")
    file.write("\n"+nimi+" - "+zanr)
    file.close()
    
def kustutaFilm(nimi):
    file = open("filmid.txt","r",encoding="UTF-8")
    data = file.readlines()
    nimed = []
    for i in range(len(data)):
        nimed.append(data[i][:data[i].index(" - ")].strip())
    file.close()
    del data[nimed.index(nimi)]
    
    file = open("filmid.txt","w",encoding="UTF-8")
    for line in data:
        file.write(line)
    file.close()
    
    
#loetleFilmid("märul")
#lisaFilm("jeesus","jesuid")
#kustutaFilm("Moana")