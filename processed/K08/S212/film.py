def loetleFilmid(genre):
    f = open('filmid.txt','r', encoding='utf8')
    lines = f.readlines()
    f.close()
    andmed = []
    filmid = []
    genres = []

    for line in lines:
        andmed += line.strip().split(' - ')
    for i in range(int(len(andmed)/2)):
        i *= 2
        filmid += [andmed[i]]
        i += 1
        genres += [andmed[i]]
    i = genres.count(genre)
    if i == 0:
        return []
    films = []
    m=0
    j=-1
    while m<i:
        j = genres.index(genre,j+1,len(genres))
        films += [filmid[j]]
        m+=1
    return films

def lisaFilm(uusFilm, uusGenre):
    f = open('filmid.txt','r', encoding='utf8')
    text = f.read()
    f.close()
    f = open('filmid.txt','a', encoding='utf8')
    if not text == '':
         f.write('\n' + uusFilm + " - " + uusGenre)
    else:
        f.write(uusFilm + " - " + uusGenre)
    f.close()
def kustutaFilm(film):
    f = open('filmid.txt','r', encoding='utf8')
    lines = f.readlines()
    f.close()
    filmid = []
    genres = []
    andmed = []
    
    for line in lines:
        andmed += line.strip().split(' - ')
    for i in range(int(len(andmed)/2)):
        i *= 2
        filmid += [andmed[i]]
        i += 1
        genres += [andmed[i]]
    index = -1
    if film in filmid:
        index = filmid.index(film)
    if not index == -1:
        lines[index] = ''
        f = open('filmid.txt','w', encoding = 'utf8')
        for line in lines:
            f.write(line)
        f.close()
