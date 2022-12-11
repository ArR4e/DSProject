import codecs

def loetleFilmid(zanr):
    f = open("filmid.txt", "r")
    filmid = [line.strip().split(' - ') for line in f]
    f.close()
    
    result = []
    for i in filmid:
        if i == "":
            continue
        elif i[1] == zanr:
            result.append(i[0])
    
    return result

def lisaFilm(film, zanr):
    f = open("filmid.txt", "a")
    if len(film) == 1:
        f.write(film + " - " + zanr + "\n")
    else:    
        f.write(" ".join(film)+ " - " + zanr + "\n")
    f.close()

def kustutaFilm(film):
    f = open("filmid.txt", "r")
    lines = f.read().splitlines()
    f_2 = open("filmid.txt", "w")
    for i in lines:
        if film not in i:
            f_2.write(i + "\n")
            
    f.close()
    f_2.close()