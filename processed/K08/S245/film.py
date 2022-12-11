fail = open('filmid.txt', encoding = 'utf-8')
zanr = str(input('Sisestage zanri nimi: '))
lisatav_nimi = str(input('Sisestage uue filmi nimi: '))
lisatav_zanr = str(input('Sisestage uue zanri nimi: '))
kustutatav_film = str(input('Millist filmi soovite kustutada: '))
def loetleFilmid(zanr):
    multikad = [0, 4]
    märul = [1, 3]
    õudukas = [2, 5]
    
    read1 = []
    read2 = []
    read3 = []
    
    for i, rida1 in enumerate(fail):
        
        if i in multikad:
            read1.append(rida1.strip().replace(' - multikas', ''))
        elif i in märul:
            read2.append(rida1.strip().replace(' - märul', ''))
        else:
            read3.append(rida1.strip().replace(' - õudukas',''))
    if zanr == 'multikas':
        print(read1)
    elif zanr == 'märul':
        print(read2)
    elif zanr == 'õudukas':
        print(read3)
    else:
        print('Sellist zanr pole!')
    
def lisaFilm(lisatav_nimi, lisatav_zanr):
    fail = open('filmid.txt','w', encoding = 'utf-8')
    fail.write(lisatav_nimi, ' - ', lisatav_zanr)
    #ei tea miks kustutab faili sisu ära ja ei kirjuta juurde

    
def kustutaFilm(kustutatav_film):
    if 
    
loetleFilmid(zanr)
lisaFilm(lisatav_nimi, lisatav_zanr)
fail.close()
        