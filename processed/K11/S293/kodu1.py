

def seosta_lapsed_ja_vanemad(x,y):
    f=open(x, encoding="UTF-8")
    f2=open(y, encoding="UTF-8")
    isikukoodid={}
    vanemadhulk=set()
    nimed={}
    for rida2 in f2:
       rida2=rida2.strip().split(" ", 1)
       nimed[rida2[0]]=rida2[1]
       
    for rida in f:
        rida=rida.strip().split()
        laps=nimed[rida[1]]
        vanem=nimed[rida[0]]
        vanemad=set()
        if laps not in isikukoodid:
            vanemad.add(vanem)
        if laps in isikukoodid:
            vanemad=isikukoodid[laps]
            vanemad.add(vanem)
            
        isikukoodid[laps]=vanemad
            

    f.close()
    f2.close()
    return isikukoodid
    

        
print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))