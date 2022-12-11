
def seosta_lapsed_ja_vanemad(f,g):
    f=open(f, encoding = "UTF-8")
    g=open(g, encoding = "UTF-8")
    vastus={}
    s={}
    
    for kood in g:
        kood=kood.strip().split(" ",1)
        s[kood[0]]=kood[1]

    for kontroll in f:
        kontroll=kontroll.strip().split()
        
        if s[kontroll[1]] in vastus:
            vastus[s[kontroll[1]]].add(s[kontroll[0]])
               
        else:
            vastus[s[kontroll[1]]]=set()
            vastus[s[kontroll[1]]].add(s[kontroll[0]])
            
    return vastus


seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")