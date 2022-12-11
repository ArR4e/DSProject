f = input("Sisesta failinimi: ")
fail = open(f,"r")
s = []

#muudab kella ajad komaarvudeks
for rida in fail:
    m = rida.replace(":30",".5").replace(":15",".25").replace(":45",".75").replace(":00","")
    t = []
    er = m.strip().split(" ")
    for i in er:
        t.append(float(i))
    s.append(t)
fail.close()
#print(s)

#järjestab kasvavasse järjekorda (kodu2 põhjal)
for i in range(len(s)-1):
    for j in range(len(s)-i-1):
        if s[j][:2]>s[j+1][:2]:
            suurem = s[j]
            s[j] = s[j+1]
            s[j+1] = suurem

fail = open(f,"r")

#tekitab järjendi ridadest
r = []
for rida_2 in fail:
    g = rida_2.strip().split(" ")
    r.append(g)
fail.close()
#print(r)

#järjestab kasvavasse järjekorda (kodu2 põhjal)
pikkus=len(r)
for i in range(pikkus-1):
    for j in range(pikkus-i-1):
        if r[j][:2]>r[j+1][:2]:
            suurem = r[j]
            r[j] = r[j+1]
            r[j+1] = suurem

#arvutab sõidu aja
p = []
for l in s:
    w = []
    aeg = l[1]-l[0]
    hind = l[2]
    w.append(aeg)
    w.append(hind)
    p.append(w)
print(p)

#otsib milline aeg on kõige väiksem ja millisel neist on odavaim hind
vähim = 1000
hind_v = 1000
d = set()
for b in range(len(p)):
    if p[b][0] < vähim:
        vähim = p[b][0]
for b in range(len(p)):
    if p[b][0] == vähim:
        if p[b][1] < hind_v:
            hind_v = p[b][1]
        
q = set()
for x in range(len(p)):
    if p[x][0] > vähim and p[x][1] < hind_v:
        q.add(x)

# otsib välja need, mis on lühima ajaga
for z in range(len(p)):
    if p[z][0] == vähim:
        q.add(z)
#print(q)
    
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for h in q:
    print(str(r[h][0])+str(" ")+str(r[h][1])+str(" ")+str(r[h][2]))
    
        
    