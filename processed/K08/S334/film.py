def loetleFilmid(genre):
    glist = []
    f = open('filmid.txt', encoding='utf8')
    for i in f.readlines():
        if i.strip().split(' - ')[1] == genre:
            glist.append(i.strip().split(' - ')[0])
    print(glist)
    f.close()
    return glist

def lisaFilm(nimi, genre):
    f = open("filmid.txt", "a", encoding='utf8')
    f.write(f'{nimi} - {genre}')
    f.close()

def kustutaFilm(nimi):
    m = []
    f = open("filmid.txt", "r", encoding='utf8')
    for i in f.readlines():
        m.append(i.strip().split(' - '))
    f.close()
    open('filmid.txt', 'w').close()
    f = open('filmid.txt', 'w', encoding='utf8')

    for i in m:
        if i[0] != nimi:
            f.write(f'{i[0]} - {i[1]}\n')
    f.close()
kustutaFilm("Moana")