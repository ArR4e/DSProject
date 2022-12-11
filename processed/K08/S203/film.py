def loetleFilmid(zanr):
    fail = open('filmid.txt', 'r', encoding='utf-8')
    selles_zanris = []
    for rida in fail:
        sisu = rida.split(' - ')
        zanr_fail = sisu[-1].strip()
        nimi = sisu[0].strip()
        if zanr_fail == zanr:
            selles_zanris.append(nimi)
    fail.close()
    return selles_zanris       
    
def lisaFilm(nimi, zanr):
    fail = open('filmid.txt', 'r', encoding='utf-8')
    järjend = fail.readlines()
    fail.close()
    uus = open('filmid.txt', 'w', encoding='utf-8')
    uus_tekst = '\n' + str(nimi) + ' - ' + str(zanr)
    järjend.append(uus_tekst)
    for el in järjend:
        uus.write(el)
    uus.close()
  
    
def kustutaFilm(nimi):
    fail = open('filmid.txt', 'r+', encoding='utf-8')
    järjend = fail.readlines()
    if isinstance(nimi, str) == True:
        for el in järjend:
            if el.startswith(nimi) == True:
                elemendi_nr = järjend.index(el)
                järjend.pop(elemendi_nr)
        fail.close()
        fail = open('filmid.txt', 'w', encoding='utf-8')
        for el in järjend:
            fail.write(el)
    else:
        for el in järjend:
            if el.startswith(nimi) == True:
                elemendi_nr = järjend.index(el)
                järjend.pop(elemendi_nr)
        fail.close()
        fail = open('filmid.txt', 'w', encoding='utf-8')
        for el in järjend:
            fail.write(el)
    fail.close()

#loetleFilmid(input("Sisestage filmi zanr: "))
#lisaFilm(input("Sisestage filmi nimi: "), input("Sisestage zanr: "))
#kustutaFilm(input("Sisesta filmi nimi: "))
