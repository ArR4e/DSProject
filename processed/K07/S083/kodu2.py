with open('taksohinnad.txt', encoding='utf-8') as f:
    x = f.readlines()

s = float(input('Sisesta tee pikkus kilomeetrites: '))

n=0
taksoHinnad=[]
taksod=[]
while n<len(x):
    if x =='':
        break
    takso = x[n].strip().split(',')
    taksod.append(takso[0])
    taksohind = float(takso[1])+float(takso[2])*s
    taksoHinnad.append(taksohind)
    n+=1
    
if x == []:
    print('Failis pole midagi sisestatud.')
else:
    odavaim = min(taksoHinnad)
    indeks = taksoHinnad.index(odavaim)
    print('Kõige odavam oli', taksod[indeks])
