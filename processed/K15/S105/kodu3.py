fnimi = input("Sisesta failinimi: ")
fail = open(fnimi, "r")

v2ljumised=[]
saabumised=[]
hinnad=[]
sobib=[]

for rida in fail:
    rida=rida.strip()
    rida=rida.split(" ")
    v2ljumised.append(rida[0])
    saabumised.append(rida[1])
    hinnad.append(rida[2])
    
for i in range(len(v2ljumised)):
    x=v2ljumised[i].split(":")
    v2ljumised[i]=(x[0], x[1])
    y=saabumised[i].split(":")
    saabumised[i]=(y[0], y[1])
    
for el in v2ljumised:
    sobib.append(el)
for el in saabumised:
    sobib.append(el)
for el in hinnad:
    sobib.append(el)

for i in range(len(hinnad)):
    for j in range(len(hinnad)):
        if (v2ljumised[i][0]<v2ljumised[j][0] or (v2ljumised[i][0]==v2ljumised[j][0] and v2ljumised[i][1]<v2ljumised[j][1])) and (saabumised[i][0]>saabumised[j][0] or (saabumised[i][0]==saabumised[j][0] and saabumised[i][1]>saabumised[j][1])) and (int(hinnad[i])>int(hinnad[j])):
            sobib.remove(v2ljumised[i])
            sobib.remove(saabumised[i])
            sobib.remove(hinnad[i])
            break
        
v=len(sobib)//3

for i in range(v*2):
    sobib[i]=int(sobib[i][0]+sobib[i][1])
    
sobibajad=[]
sobibhinnad=[]

for i in range(v):
    sobibajad.append((sobib[i], sobib[i+v]))
    sobibhinnad.append(sobib[i+2*v])
    

for i in range(len(sobibajad)):
    key=sobibajad[i][0]
    key1=sobibajad[i][1]
    hkey=sobibhinnad[i]
    j=i-1
    while j>=0 and key<sobibajad[j][0]:
        sobibajad[j+1]=(sobibajad[j][0], sobibajad[j][1])
        sobibhinnad[j+1]=sobibhinnad[j]
        j-=1
    sobibajad[j+1]=(key, key1)
    sobibhinnad[j+1]=hkey
    
for i in range(len(sobibajad)):
    if int(sobibajad[i][0])<1000:
        sobibajad[i]=("0"+str(sobibajad[i][0]), sobibajad[i][1])
   
for i in range(len(sobibajad)):
    print(str(sobibajad[i][0])[0:2]+":"+str(sobibajad[i][0])[2:4]+" "+str(sobibajad[i][1])[0:2]+":"+str(sobibajad[i][1])[2:4]+" "+str(sobibhinnad[i])) 