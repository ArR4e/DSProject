#loetleme vastavalt argumendile sobivad filmid
def loetleFilmid(žanr):

    f=open('filmid.txt', encoding= 'UTF-8')
    read=f.readlines()#loeme kõik read sisse
    nimed=[] #siia koondame kõik filmi nimed
    for i in range (len(read)):
        element= read[i].split(' - ')
        nime_el= element[0]
        žanri_el= element[1].strip('\n')
        if žanr == žanri_el:
            nimed= nimed + [nime_el] #koondame sobivad nimed siia
    f.close()
    return nimed

#lisame filmi faili lõppu
def lisaFilm (nimi, žanr):
    f= open('filmid.txt','a',encoding= 'UTF-8') #avame faili ja kirjutame lõppu
    sisu= ('\n'+nimi+' - '+žanr+'\n')
    f.write(sisu)
    f.close()
    
#kustutame soovitud filmi
def kustutaFilm (nimi):
    #nimi= 'Avengers: End Game'
    f=open('filmid.txt', encoding= 'UTF-8') #ainult avame, et andmed saada
    read=f.readlines()#loeme kõik read sisse
    for i in range (len(read)): #võtame read element haaval ette
        element= read[i].split(' - ')
        nime_el= element[0]
        if nime_el== nimi:
            #print('leitud',nimi)
            nimekiri= read[:i]+read[(i+1):]
    f.close()
    f=open('filmid.txt','w',encoding= 'UTF-8') #avame uuesti ja kirjutame kogu sisu üle
    for i in range(len(nimekiri)):
        rida=(nimekiri[i])
        f.write(rida)
    f.close() #sulgeme faili
