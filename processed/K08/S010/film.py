def loetleFilmid(žanr):
    f=open('filmid.txt', encoding='UTF-8')
    sisu=f.readlines()
    filmidelist=[]
    for element in sisu:
        if žanr in element.strip():
            filmidelist+=[element.split(' - ')[0]]
    f.close()
    return filmidelist

def lisaFilm(nimi, žanr):
    a=open('filmid.txt', encoding='utf-8')
    sisu=a.read()
    a.close()
    f=open('filmid.txt', mode='w', encoding='utf-8')
    f.write(sisu+'\n'+nimi+' - '+žanr + '\n')
    f.close()
    
def kustutaFilm(nimi):
    a=open('filmid.txt', encoding='utf-8')
    sisulist=a.readlines()
    õige_sisulist=[]
    for element in sisulist:
        if nimi not in element.strip():
            õige_sisulist+=[element]
    a.close()
    f=open('filmid.txt', mode='w', encoding='utf-8')
    for element1 in õige_sisulist:
        f.write(element1)
    f.close()
    