info=[]
f=open("taksohinnad.txt","r",encoding="utf8")
for rida in f:
    info.append(rida.strip("\n").split(","))
f.close()
def sõit(n):
    hinnad=[]
    firmad=[]
    i=0
    try:
        while i<len(info):
            for k in info:
                firmad.append(info[i][0])
                hinnad.append(float(info[i][1])+float(info[i][2])*n)
                i+=1
        vähim=hinnad.index(min(hinnad))
        return firmad[vähim]
    except:
        return(0,0)
km=float(input("Sisesta tee pikkus kilomeetrites: "))
print("Kõige odavam on "+str(sõit(km))+'.')