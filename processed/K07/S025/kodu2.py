def taksohind(alg, km):
    hind = alg + a * km
    return hind

f = open('taksohinnad.txt', encoding='utf-8')
a = float(input('Sisesta tee pikkus kilomeetrites: '))
nimed = []
taksode_hinnad = []
for rida in f:
    c = rida.strip('\n')
    b = c.split(',')
    nimi = b[0]
    sisse = float(b[1])
    kilomeetri_hind = float(b[2])
    d = taksohind(sisse, kilomeetri_hind)
    nimed.append(nimi)
    taksode_hinnad.append(d)
try:
    väikseim_hind = min(taksode_hinnad)
    indeks = taksode_hinnad.index(väikseim_hind)
    odavaim = nimed[indeks]
    print('Kõige odavam on ' + odavaim + '.')
except ValueError:
    print('Tühi hinnakiri.')
f.close()