def loetleFilmid(zanr):
    fail=open('filmid.txt', encoding='UTF-8')
    järjend_ridadest= fail.read().splitlines()
    järjend_ridadest_kus_zanr=[]
    for el in järjend_ridadest:
        if zanr in el:
            i=el.rfind('-')
            järjend_ridadest_kus_zanr.append(el[:i].strip())
    fail.close()
    return järjend_ridadest_kus_zanr

def lisaFilm(nimi, zanr):
    filmisõne=nimi+' - '+zanr
    fail=open('filmid.txt','a', encoding='UTF-8',)
    fail.write('\n'+filmisõne)
    fail.close()
    
def kustutaFilm(film):
    try:
        with open('filmid.txt', 'r', encoding='UTF-8') as fail:
            ridadejärjend=fail.readlines()
            for el in ridadejärjend:
                if film in el:
                    kustutatav=el
            ridadejärjend.remove(kustutatav)
            normsõne=''.join(ridadejärjend)
        with open('filmid.txt', 'w', encoding='UTF-8') as f:
            f.write(normsõne)
        return None
    except:
        return False