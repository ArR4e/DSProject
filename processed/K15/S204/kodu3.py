d=[]
g=[]
u=[]
fail = open("buss.txt", encoding="UTF-8")

for rida in fail:
    start, end, hind = rida.split(" ")
    start1, start2 = start.split(":")
    if int(start1[0])==0:
        start1=start1[1: ]
    end1, end2 = end.split(":")
    if int(end[0])==0:
        end1=end1[1: ]
    vahemik=(int(end1)-int(start1))*60+(int(end2)-int(start2))
    d.append(vahemik)
    g.append(rida.strip())


#print (d)
#print(g)
x=0
for el in d:
    if el == min(d):
        u=d.index(el)
        
        #print(u)
        print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")
        print(g[u])
        d.remove(d[x])
        x+=1