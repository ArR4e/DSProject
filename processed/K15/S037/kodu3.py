fail=input("Sisestage failinimi: ")
f=open(fail,'r')
järj=[]
for rida in f:
    järj += rida.strip().split(' ')
    
mittesobilikud = []
väljumised=järj[::3]
saabumised=järj[1::3]
for i in range(len(väljumised)-1):
    for e in range(1,len(väljumised)):
        if väljumised[i] < väljumised[e]:
            if saabumised[i] > saabumised[e]:
                mittesobilikud += [väljumised[i]]

for el in mittesobilikud:
    i = järj.index(el)
    for kordi in range(3):
        järj.remove(järj[i])
    
print(" Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for i in range(int(len(järj) / 3)):
    e = i*3
    väljumine=järj[e]
    saabumine=järj[e+1]
    pilet=järj[e+2]
    print(f'{väljumine} {saabumine} {pilet}')