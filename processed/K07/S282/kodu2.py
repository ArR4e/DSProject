teepikkus=input('Sisestage teepikkus koju: ')
f=open('taksohinnad.txt')
hinnad=[]
nimed=[]
for rida in f:
    rida=rida.strip()
    andmed=rida.split(',')
    hinnad.append(float(andmed[1])+float(andmed[2])*float(teepikkus))
    nimed.append(andmed[0])
vahim=hinnad.index(min(hinnad))
nimi=nimed[vahim]
print('Kõige odavam on '+nimi)
f.close()