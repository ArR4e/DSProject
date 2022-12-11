tee = float(input('Sisesta tee pikkus(km): '))
n = 0
hind = []
nimed = []

file = open('taksohinnad.txt', 'r', encoding = 'UTF-8')
for i in file:
    n = n + 1
    a = i.split(',')
    nimi = (a[0])
    stardihind = float(a[1])
    km_hind = float(a[2])
    uus_hind = stardihind + tee * km_hind
    hind.append(uus_hind)
    nimed.append(nimi)

if n == 0:
    print('Failis sellist ei ole')
else:
    väiksem = min(hind)
    ind = hind.index(väiksem)
    nimetus = nimed[ind]
    print('Odavam on ', nimetus, '.', sep='')