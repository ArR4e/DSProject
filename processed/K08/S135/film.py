def loetleFilmid(zanr):
    filmid = []
    f = open('filmid.txt', encoding = 'UTF-8')
    
    for line in f:
        film = line.split(' - ')
        if film[1].strip() == zanr:
            filmid.append(film[0])
        else:
            continue
    
    f.close()
    return filmid

def lisaFilm(nimi, zanr):
    f = open('filmid.txt', encoding = 'UTF-8')
    hasNewline = False
    if f.read().endswith('\n'):
        hasNewline = True
    f.close()
    
    f = open('filmid.txt', 'a', encoding = 'UTF-8')
    if hasNewline:
        f.write(nimi + ' - ' + zanr)
    else:
        f.write('\n' + nimi + ' - ' + zanr)
    f.close()
    
def kustutaFilm(nimi):
    f = open('filmid.txt', encoding = 'UTF-8')
    films = []
    for line in f:
        if line.split(' - ')[0] != nimi:
            films.append(line)
    f.close()
    
    f = open('filmid.txt', 'w', encoding = 'UTF-8')
    f.writelines(films)
    f.close()