def järjesta_punktid(p):
    for i in range(len(p)-1):
        for j in range(i, len(p)):
            if p[j][0]<p[i][0]:
                p[i], p[j]= p[j], p[i]
            

f=open(input('Mis on bussifaili nimi?'))
ajad=[]
for rida in f:
    ajad.append(rida.strip().split())
    
järjesta_punktid(ajad)

i=0
pikkus=len(ajad)
while i<pikkus:
    for j in range(i+1, pikkus):
        
        if ajad[i][1]>ajad[j][1] and float(ajad[i][2])>float(ajad[j][2]):
            ajad.pop(i)
            i-=1
            pikkus-=1
            break
    i+=1
   
for rida in ajad:
    for el in rida:
        print(el, end=' ')
    print('')