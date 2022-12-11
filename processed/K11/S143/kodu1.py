def seosta_lapsed_ja_vanemad(l,n):
    d = {}
    d1 = {}
    with open(l,"r",encoding="UTF-8") as f:
        with open(n,"r",encoding="UTF-8") as g:
            kln = list(map(lambda x: x.split(" "),f.read().strip().split("\n")))
            #print(kln)
            for x in list(map(lambda x: x.split(" ",1),g.read().strip().split("\n"))):
                d[x[0]]=x[1]
    for x in kln:
        if d[x[1]] not in d1.keys():
            d1[d[x[1]]] = set([d[x[0]]])
        else:
            d1[d[x[1]]].add(d[x[0]])
    return d1

a = seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")
print(a)

for x in a.keys():
    print(f"{x}: {', '.join(a[x])}")
