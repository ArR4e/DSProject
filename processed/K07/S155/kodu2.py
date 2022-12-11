kodutee = float(input('Sisesta tee pikkus kilomeetrites: '))
f = open('taksohinnad.txt', encoding = 'UTF-8')
hinnad = []
teenusepakkujad = []
for rida in f:
    lause = rida.strip()
    jupid = lause.split(",")
    teenusepakkujad += [jupid[0]]
    istumine = float(jupid[1])
    km_hind = float(jupid[2])
    hinnad += [kodutee*km_hind + istumine]

odavaim = min(hinnad)
indeks = hinnad.index(odavaim)
print('Kõige odavam on {}'.format(teenusepakkujad[indeks]))
