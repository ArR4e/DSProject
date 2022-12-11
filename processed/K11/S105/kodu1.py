def seosta_lapsed_ja_vanemad(a,b):
    f=open(a,"r",encoding="UTF-8")
    g=open(b,"r",encoding="UTF-8")
    lapsedjavanemad=dict()
    nimeds=dict()
    readg=[]
    readf=[]
    ikd=[]
    nimed=[]
    nimi=""
    i=0
    for rida in g:
        rida=rida.strip()
        readg=rida.split(" ")
        ikd.append(readg[0])
        readg.remove(readg[0])
        nimi=" ".join(readg)
        nimed.append(nimi)
    while i<len(nimed):
        nimeds[ikd[i]]=nimed[i]
        i+=1
    for rida in f:
        rida=rida.strip()
        readf=rida.split()
        lapsedjavanemad[nimeds[readf[1]]]=set()
    f.close()
    f=open(a,"r",encoding="UTF-8")
    for rida in f:
        rida=rida.strip()
        readf=rida.split()
        lapsedjavanemad[nimeds[readf[1]]].add(nimeds[readf[0]])
    f.close()
    g.close()
    
    return lapsedjavanemad

andmed=seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")
print(andmed)

for el in andmed:
    print(el, end=": ")
    for el in andmed[el]:
        print(el, end=" ")
    print("\n")

    