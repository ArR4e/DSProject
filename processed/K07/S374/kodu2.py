kilomeetrid = float(input('Sisesta tee pikkus kilomeetrites: '))

f = open('taksohinnad.txt', encoding='UTF-8')

taksod = []
hinnad = []

for rida in f:
    elemendid = rida.split(',')
    
    for el in elemendid:
        taksod.append(el.strip())
    
f.close()


for i in range(1, len(taksod), 3):
    hind = float(taksod[i]) + kilomeetrid*float(taksod[i+1])
    hinnad.append(hind)
    
try:
    miinimumIndex = hinnad.index(min(hinnad))
    odavaimTakso = taksod[miinimumIndex*3]
    print('Koige odavam on '+odavaimTakso+'.')
    
except:
    print('Puudub takso.')
