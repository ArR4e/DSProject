def loetleFilmid(žanr):
    i = 0
    žanrivalik = []
    while i < len(žanrid):
        if žanr in žanrid[i]:
            žanrivalik.append(nimed[i])
        i += 1
    return žanrivalik

def lisaFilm(nimi, žanr):
    with open('filmid.txt', 'a', encoding = 'UTF-8') as f:
        print('\n' + nimi + ' - ' + žanr, file = f)
    return 'Film lisatud!'

def kustutaFilm(nimi):
    y = 0
    with open('filmid.txt', encoding = 'UTF-8') as f:
        read = f.readlines()
        muudetud_read = []
        for element in read:
            muudetud_read.append(element.strip())
    with open('filmid.txt', 'w', encoding = 'UTF-8') as f:
        for rida in muudetud_read:
            if nimi not in muudetud_read[y]:
                f.write(rida)
                f.write('\n')
            y += 1
    return 'Film kustutatud!'

with open('filmid.txt', encoding = 'UTF-8') as f:
    nimed = []
    žanrid = []
    for rida in f:
        rea_osa = rida.split(' - ')
        nimed.append(rea_osa[0].strip())
        žanrid.append(rea_osa[1].strip())