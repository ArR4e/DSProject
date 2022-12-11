tee = float(input('Sisesta tee pikkus kilomeetrites: '))
fail = open('taksohinnad.txt')
a = fail.readline()
hinnad = []
nimed = []
while a != '':
    a = a.split(',')
    hind = float(a[1])+tee*float(a[2])
    hinnad.append(hind)
    nimi = str(a[0])
    nimed.append(nimi)
    a = fail.readline()
if hinnad == []:
    print('')
else:
    g = hinnad.index(min(hinnad))  
    print('Kõige odavam on',nimed[g]+'.')
fail.close()


    

    
    
    