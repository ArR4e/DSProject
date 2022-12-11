def loetleFilmid(žanr):
    f=open('filmid.txt',encoding='UTF-8')
    loetelu=[]
    for rida in f:
        rida=rida.strip('\n').split(' - ')
        if rida[-1]==žanr:
            loetelu.append(rida[0])
    f.close()
    return loetelu

def lisaFilm(nimi,žanr):
    f=open('filmid.txt',encoding='UTF-8')
    read=f.read()
    loetelu=read.split("\n")
    uus_film=nimi+' - '+žanr
    loetelu.append(uus_film)
    f.close()
    f=open('filmid.txt','w',encoding='UTF-8')
    f.write("\n".join(loetelu))
    f.close()
def kustutaFilm(film):
    uus_sisu=[]
    f=open('filmid.txt','r',encoding='UTF-8')
    for rida in f:
        rida=rida.strip().split('-')
        if rida[0]!=film+' ':
            uus_sisu.append('-'.join(rida))
    f.close
    f=open('filmid.txt','w',encoding='UTF-8')
    f.write('\n'.join(uus_sisu))
    f.close()

