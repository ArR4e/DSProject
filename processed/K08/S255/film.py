def loetleFilmid(zanr):
    nimed = []
    with open('filmid.txt', 'r', encoding='utf-8') as loe_fail:
        for i in loe_fail:
            jarjend = i.split(' - ')
            a = str(jarjend[1].strip())
            jarjend[1] = a
            if jarjend[1] == zanr:
                nimed.append(jarjend[0])
        return nimed


def lisaFilm(nimi, zanr):
    with open('filmid.txt', 'a', encoding='utf-8') as lisa_juurde:
        a = (f'\n{nimi} - {zanr}')
        lisa_juurde.write(a)
    

def kustutaFilm(nimi):
    with open('filmid.txt', 'r', encoding='utf-8') as loe:
        rida = loe.readlines()
    with open('filmid.txt', 'w+', encoding='utf-8') as kirjuta_ule:
        for i in rida:
            if i.startswith(nimi):
                
                continue
            else:
                kirjuta_ule.write(i)