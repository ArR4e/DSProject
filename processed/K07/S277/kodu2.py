pikkus = 0
while pikkus == 0:
    pikkus = float(input('Sisestage tee pikkus kilomeetrites: '))
nimed = []
taksode_hinnad = []

f = open('taksohinnad.txt', 'r', encoding = 'utf-8')

for i in f:
    i = i.strip().split(',')
    
    nimed.append(i[0])
    taksode_hinnad.append(float(i[1]) + float(i[2]) * pikkus)
    
indeks = 0
miinimum = taksode_hinnad[0]
for i in range(len(taksode_hinnad)):
    if taksode_hinnad[i] < miinimum:
        miinimum = taksode_hinnad[i]
        indeks = i

print('Odavaim on', nimed[indeks] + '.')
