

def erinevad_sümbolid(y):
    x=set()
    for i in y:
        if i not in x:
            x.add(i)
    return x

def sümbolite_sagedus(y):
    x={}
    for i in y:
        x[i]=x.get(i,0)+1
    return x

def grupeeri(y):
    taishäälikud="a,e,i,o,u,õ,ä,ö,ü"
    kashäälikud="v,j,l,m,n,r,s,h,f,š,z,ž,g,k,b,p,d,t"
    x={"Täishäälikud":{},"Kaashäälikud":{},"Muud":{}}
    k={}
    for i in y:
        k[i]=k.get(i,0)+1
    for i in k:
        t=(i,k[i])
        if i in taishäälikud:
            x["Täishäälikud"].update([t])
        elif i in kashäälikud:
            x["Kaashäälikud"].update([t])
        else:
            x["Muud"].update([t])
                   
    return x
print(grupeeri("elegant"))
# x["täishäälikud"].update([t])