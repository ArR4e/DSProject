def loetleFilmid(zanr):
    fail = open("filmid.txt", "r", encoding = 'UTF-8')
    try:
        lines = fail.read().split('\n')
        filmid = []
        for line in lines:
            film = line.split(' - ')
            if film[1] == zanr:
                filmid.append(film[0])
        fail.close()
        return filmid
    except:
        return []
        
            
def lisaFilm(nimi, zanr):
    fail = open("filmid.txt", "r", encoding = 'UTF-8')
    lines = fail.read().split('\n')
    fail.close()
    lines.append(nimi + ' - ' + zanr)
    text = '\n'.join(lines)
    fail = open("filmid.txt", "w", encoding = 'UTF-8')
    fail.write(text)
    fail.close()
    
    
def kustutaFilm(nimi):
    fail = open("filmid.txt", "r", encoding = 'UTF-8')
    lines = fail.read().split('\n')
    lines_new = []
    for line in lines:
        film = line.split(' - ')
        if film[0] != nimi:
            lines_new.append(line)
    fail.close()
    text = '\n'.join(lines_new)
    fail = open("filmid.txt", "w", encoding = 'UTF-8')
    fail.write(text)
    fail.close()
    
    
print(loetleFilmid("multikas"))
#lisaFilm('Harry Potter', 'fantaasia')
#kustutaFilm('Harry Potter')
