def loetleFilmid(žanr):
    f = open('filmid.txt', 'r+', encoding='UTF-8')
    
    loetelu = []
    
    for rida in f:
        if rida.strip().split(' - ')[1] == žanr:
            loetelu = loetelu + [rida.strip().split(' - ')[0]]
        if rida == '':
            break
    print(loetelu)
    return loetelu

def lisaFilm(nimi, žanr):
    f = open('filmid.txt', 'a', encoding='UTF-8')
    
    f.write('\n' + nimi + ' - ' + žanr)

def kustutaFilm(nimi):
    f = open('filmid.txt', 'r', encoding='UTF-8')
    read = f.readlines()
    f.close()
    
    f = open('filmid.txt', 'w', encoding='UTF-8')
    for rida in read:
        if rida.strip().split(' - ')[0] != nimi:
            f.write(rida)
    f.close()