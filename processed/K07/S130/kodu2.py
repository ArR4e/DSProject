teepikkus = float(input('Teepikkus kilomeetrites: '))
fail = open('taksohinnad.txt', encoding = 'UTF-8')
taksode_hinnad = []
nimed = []
for rida in fail:
    osad = rida.strip().split(',')
    taksonimi = osad[0]
    nimed.append(taksonimi)
    stardihind = float(osad[1])
    kilomeetri_hind = float(osad[2])
    hind = stardihind + teepikkus*kilomeetri_hind
    taksode_hinnad.append(hind)
try:
    vaikseim = min(taksode_hinnad)
    indeks = taksode_hinnad.index(vaikseim)
    odavaim = nimed[indeks]
except ValueError:
    odavaim = ('Taksot pole vaja')

print('Koige odavaim on', odavaim)

fail.close()