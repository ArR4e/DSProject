
def loetleFilmid(zanr):
    f=open("filmid.txt", encoding='utf-8')
    read=f.readlines()
    f.close()
    
    filmid=[]
    zanrid=[]
    for el in read:
        el=el.strip('\n')
        el=el.split(' - ')
        filmid= filmid + [el[0].strip()]
        zanrid= zanrid + [el[1].strip()]
    loetelu=[]
    l=0
    while l < len(filmid):
        if zanrid[l]==zanr:
            loetelu=loetelu + [filmid[l]]
            l += 1
        else:
            l +=1
    
    return loetelu

def lisaFilm(nimi,z):
    tekst=('\n' + nimi + ' - ' + z)
    with open('filmid.txt','a+') as f:
        f.write(tekst)
        f.close()

def kustutaFilm(nimi):
    f=open('filmid.txt')
    read=f.readlines()
    f.close()
    uus=open('filmid.txt','w')
    for rida in read:
        if nimi in rida:
            continue
        else:
            uus.write(rida)
    uus.close()
    