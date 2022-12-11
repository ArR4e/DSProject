fail = open('filmid.txt')
rada = fail.readline().strip()
a = 0
kordi = 0
b = 0
#while rada != '':
 #   a = a+1
  #  rada = fail.readline().strip()
#fail.seek(0)
#fail.close()
multikad = []
def loetleFilmid(Znimi):
    fail = open('filmid.txt')
    kordi = 0
    a = 0
    rada = fail.readline().strip()
    while rada != '':
        a = a+1
        rada = fail.readline().strip()
    fail.seek(0)
    fail.close()
    fail = open('filmid.txt',encoding = 'utf-8')
    while kordi < a:   
        rada = fail.readline().strip()
        rida = rada.split(' - ')
        sõna = rida[-1]
        if sõna == Znimi:
            multikad.extend(rida[:-1])
            kordi = kordi+1
    #return (multikad)
        elif rada == '':
            #multikad.append(rada)
            kordi = kordi + 1
    return (multikad)
            #kordi = kordi+1
    fail.seek(0)
    fail.close()
def lisaFilm(nimi,zanr):
    #while kordi > False:
    fail = open('filmid.txt','a')
    kokku = (nimi+' - '+zanr)
    fail.write('\n')
    fail.write(kokku)

def kustutaFilm(fnimi):
    fail = open('filmid.txt')
    read = fail.readlines()
    fail.close()
    fail3 = open('filmid.txt','w')
    for rida in read:
        #fail3 = open('filmid.txt','r+')
        a = rida.strip('\n')
        a = a.strip()
        if ((a.split(' - '))[:-1]) != [fnimi]:
            fail3.write(rida)
    fail3.close()
#fail = open('filmid.txt')
#while kordi < a:   
kordi = 0
 #   kordi = kordi+1

#fail.close()


