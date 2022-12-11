failinimi=input()
f=open(failinimi,encoding="UTF-8")
sisu=f.readlines()
f.close()
for a in range(len(sisu)):
    sisu[a]=sisu[a].strip("\n")
    sisu[a]=sisu[a].split(" ")
def ajavahe(aeg1,aeg2):
    aeg1=aeg1.split(":")
    aeg2=aeg2.split(":")
    tunnid=int(aeg2[0])-int(aeg1[0])
    minutid=int(aeg2[1])-int(aeg1[1])
    if minutid<0:
        minutid+=60
        tunnid-=1
    minutid=minutid/60
    vastus=tunnid+minutid
    return(vastus)
def kiiremad(nimekiri):
    vahim=ajavahe(nimekiri[0][0],nimekiri[0][1])
    sobivad=[]
    for a in nimekiri:
        aeg=ajavahe(a[0],a[1])
        if aeg<vahim:
            vahim=aeg
            sobivad=[]
            sobivad.append(a)
        elif aeg==vahim:
            sobivad.append(a)
    return sobivad
asi=kiiremad(sisu)
for a in asi:
    for b in a:
        print(b,end=" ")
    print("")