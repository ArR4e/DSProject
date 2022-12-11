def loetleFilmid(zanr):
    f = open("filmid.txt","r", encoding='UTF-8')
    out = []
    for i in f.readlines():
        rida = i.rstrip().split(' - ')
        #kaotan algusest tyhiku, kui see eksisteerib
        rida[0] = rida[0][::-1].rstrip()[::-1]
        if rida[1] == zanr:
            out.append(rida[0])
    f.close()
    return out

def lisaFilm(nimi, zanr):
    f = open("filmid.txt", 'r', encoding='UTF-8')
    arr = f.readlines()
    lisa = ''
    if arr != []:
        lisa = arr[-1][-1] != '\n'
    f.close()
    f = open("filmid.txt","a", encoding='UTF-8')
    newline = '\n'
    f.write(f"{newline if lisa else ''}{nimi} - {zanr}{newline}")
    f.close()

def kustutaFilm(nimi):
    f = open("filmid.txt", 'r', encoding='UTF-8')
    arr = f.readlines()
    f.close()
    f = open("filmid.txt", "w", encoding='UTF-8')
    out = []
    for i in arr:
        rida = i.rstrip().split(' - ')
        #kaotan algusest tyhiku, kui see eksisteerib
        rida[0] = rida[0][::-1].rstrip()[::-1]
        if rida[0] != nimi:
            out.append(f"{rida[0]} - {rida[1]}\n")
    f.write(''.join(out))
    f.close()

