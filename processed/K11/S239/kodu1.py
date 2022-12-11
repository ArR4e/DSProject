def seosta_lapsed_ja_vanemad(fail1,fail2):
    f=open(fail1)
    g=open(fail2)

    isikukoodid={}
    isikud={}
    seotud={}
    
    i=0
    for rida in f:
        rida=rida.strip("\n")
        isikukood=rida.split(" ")
        isikukoodid[str(i)+":"+isikukood[0]]=isikukood[1]
        i+=1

    for rida in g:
        rida=rida.strip("\n")
        isik=rida.split(" ")
        isikud[isik[0]]=isik[1]+" "+isik[2]
    
    f.close()
    g.close()
    
    for i in isikukoodid:
        try:
            seotud[isikud[isikukoodid[i]]].add(isikud[i[2:]])
        except:
            seotud[isikud[isikukoodid[i]]]={isikud[i[2:]]}
    
    return seotud

for j in seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt"):
    if len(seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")[j])==2:
        vanemad=list(seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")[j])
        vanem1=vanemad[0]
        vanem2=vanemad[1]
        print(j+":",vanem1+",",vanem2)
    else:
        for l in seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")[j]:
            print(j+":",l)