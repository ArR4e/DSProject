teepikkus=float(input('Sisesta tee pikkus kilomeetrites: '))
f=open('taksohinnad.txt', encoding='UTF-8')
hind=0
hinnad=[]
nimed=[]
for rida in f:
    hinnad.append(float((rida.strip()).split(',')[-2])+float((rida.strip()).split(',')[-1])*teepikkus)
    nimed.append((rida.strip()).split(',')[0])
try:
    väikseim=min(hinnad)
    väikseim_indeks=hinnad.index(väikseim)
    väikseim_nimi=nimed[väikseim_indeks]
    print('Kõige odavam on '+ väikseim_nimi +'.')
    f.close()
except:
    print('Viga failis!')
    f.close()