from statistics import harmonic_mean
# import matplotlib.pyplot as pt
#failinimi=input("Sisesta faili nimi: ")
#read=open("failinimi")
read=open("aktsiad.txt")
alghinnad=[]
kuupäevad=[]
for i in read.readlines():
    kuupäevad+=[i.split(",")[0].strip()]
    alghinnad+=[float(i.split(",")[-1].rstrip("\n").lstrip())]

def silu_andmed(alghinnad,y):
    vahetulem=[]
    abilist=[]
    abi=0
    for i in alghinnad:
        if abi != y:
            abilist=abilist+[i]
            vahetulem+=[harmonic_mean(abilist)]
            abi+=1
        else:
            abilist.append(i)
            abilist.pop(0)
            vahetulem+=[harmonic_mean(abilist)]
    return vahetulem
        
  
# t=silu_andmed(alghinnad,3)
read.close()
# fig = pt.figure()
# ax = fig.add_subplot(1,1,1)
# ax.plot(kuupäevad,alghinnad)
# ax.plot(kuupäevad,t) 
# ax.set_xlabel("mu")
pt.show()