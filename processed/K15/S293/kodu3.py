fail=input("Sisestage failinimi: ")
f=open(fail)
järjend=[]
for rida in f:
    rida=rida.strip().split(" ")
    rida[0]=rida[0].split(":")
    x=(int(rida[0][1])/60)
    rida[0]=int(rida[0][0])+x
    
    rida[1]=rida[1].split(":")
    y=(int(rida[1][1])/60)
    rida[1]=int(rida[1][0])+y
    
    rida[2]=int(rida[2])
    
    järjend.append(rida)

def kontroll():
    for i in range(len(järjend)):
        if i<len(järjend):
            for võrdlus in range(len(järjend)):
                if võrdlus<len(järjend):
                    if võrdlus==i:
                        continue
                    elif järjend[i][0]<järjend[võrdlus][0] and järjend[i][1]>järjend[võrdlus][1] :
                        järjend.pop(i)
                        kontroll()
                    elif järjend[i][0]==järjend[võrdlus][0] and järjend[i][1]-järjend[i][0]==järjend[võrdlus][1]-järjend[võrdlus][0] and järjend[i][2]>järjend[võrdlus][2]:
                        järjend.pop(i)
                        kontroll()
                    else:
                        a=1   
kontroll()
for i in range(len(järjend)):
    lahkumine=str(järjend[i][0]).split(".")
    arv="0."+lahkumine[1]
    komaarv=float(arv)
    x=komaarv*60
    if x==0.0:
        x="00"
    else:
        x=str(int(x))
    järjend[i][0]=str(lahkumine[0])+":"+x
    
    saabumine=str(järjend[i][1]).split(".")
    arv2="0."+saabumine[1]
    komaarv2=float(arv2)
    y=komaarv2*60
    if y==0.0:
        y="00"
    else:
        y=str(int(y))
    
    järjend[i][1]=str(saabumine[0])+":"+y

järjend.sort()
print("Esimessest linnast teise sõitmiseks võiksid kaaluda järgmiseid busse")
for i in range(len(järjend)):
    print(järjend[i][0] +" "+ järjend[i][1]+ " "+ str(järjend[i][2]))
#print(järjend)
    
f.close()