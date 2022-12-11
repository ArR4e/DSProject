def loetleFilmid(žanr):
    f = open('filmid.txt', encoding='UTF-8')
    read = f.readlines()
    f.close()
    
    filmid = []
    žanrid = []
    for i in read:
        i = i.strip()
        try:
            kriips = i.index(" - ")
        except:
            break
        filmid.append(i[:kriips])
        žanrid.append(i[kriips+3:])
    järks = 0
    tulemus = []
    for k in žanrid:
        if k == žanr:
            tulemus.append(filmid[järks])
        järks += 1
    return tulemus
    
def lisaFilm(film, žanr):
    with open("filmid.txt", "a") as fail:
        fail.write('\n' + f'{film} - {žanr}')
    

def kustutaFilm(film):
    f = open('filmid.txt', encoding='UTF-8')
    read = f.readlines()
    f.close
    f = open('filmid.txt', 'w', encoding='UTF-8')
    for rida in read:
        rida = rida.strip()
        if not rida.startswith(film):
            f.write(rida + '\n')
    f.close()
