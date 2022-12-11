def loetleFilmid(žanr):
    f = open('filmid.txt' , 'r', encoding = 'UTF-8')
    väljastada = []
    failist = f.readlines()
    for rida in failist:
        f_nimi = rida.split(' - ')[0]
        f_žanr = rida.split(' - ')[1]
        if žanr.lower() == f_žanr.strip():
            väljastada.append(f_nimi)
    f.close()
    return väljastada

def lisaFilm(nimi, žanr):
    f = open('filmid.txt', 'a', encoding = 'UTF-8')
    f.write('\n' +str(nimi) + ' - ' + str(žanr))
    f.close()
    
def kustutaFilm(nimi):
    f = open('filmid.txt' , 'r', encoding = 'UTF-8')
    failist = f.readlines()
    f.close()
    f = open('filmid.txt' , 'w', encoding = 'UTF-8')
    for rida in failist:
        if nimi != rida.split(' - ')[0].strip():
            f.write(rida)
    f.close()