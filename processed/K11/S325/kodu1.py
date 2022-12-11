def seosta_lapsed_ja_vanemad(a,b):
    x={}
    koodid={}
    fn=open(b)
    fl=open(a)
    for line in fn:
        paar=line.split()
        x[paar[0]]=(paar[1]+" "+paar[2])
    for line in fl:
        paar=line.split()
        if x[paar[1]] not in koodid.keys():
            koodid[x[paar[1]]]=set()
        koodid[x[paar[1]]].add(x[paar[0]])
    #for key in koodid:
        #for i in range:
            #elem.replace(elem,x[elem])
        #key=x[key]
    return (koodid)
    

d=seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")
for key in d:
    print(key+": ",end="")
    for elem in d[key]:
        print(elem,"",end="")
    print("\n")