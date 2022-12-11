
def loetlefilmid(žanr):
    f = open("filmid.txt")
    tekst = f.readlines()
    f.close()
    #sisu = [el.split("-") for el in tekst]
    sisu = []
    for el in tekst:
        splititud = el.split(' - ')
        try:
            sisu += [splititud[0],splititud[1]]
        except:
            break
    x = 0
    filmid = []
    zanrid = []
    tagastus = []
    for el in sisu:
        if x %2 == 0:
            filmid += [el]
        else:
            zanrid += [el]
        x += 1
    x = 0
    zanrid = [a.strip()for a in zanrid]
    for a in zanrid:
        if a == žanr:
            tagastus +=[filmid[x]]
        x +=1
    return tagastus
def lisafilm(nimi,žanr):
    f = open('filmid.txt','a')
    f.write('\n'+nimi +' - ' + žanr)
    f.close()
def kustutafilm(nimi):
    f = open('filmid.txt','r')
    tekst = f.readlines()
    f.close
    f = open('filmid.txt','w')
    sisu = []
    filmid = []
    x = 0
    #splitib teksti
    for el in tekst:
        #el = el.strip()
        splititud = el.split(' - ')
        filmid += [splititud[0]]
    #filmid = [a.strip()for a in filmid]
    for film in filmid:
        if film == nimi:
            x +=1
        elif film != nimi:
            f.write(tekst[x])
            x+=1
    f.close()
print(loetlefilmid('marul'))
#k1 = input("filminimi : ")
#k2 = input("zanrinimi : ")
#lisafilm(k1,k2)
#k3 = input("kustuta : ")
#kustutafilm(k3)