teepikkus = float(input('Sisesta tee pikkus kilomeetrites: '))
fail = open("taksohinnad.txt", encoding="UTF-8")
väikseim = 100000000000000000000000000
nimi = ''
for rida in fail:
    sisu = rida.strip().split(',')
    nimetus = sisu[0]
    stardihind = float(sisu[1])
    kilomeetri_tasu = float(sisu[2])
    hind = (stardihind + teepikkus * kilomeetri_tasu)
    if hind < väikseim:
        väikseim = hind
        nimi = nimetus
        
print('Kõige odavam on ' + nimi +'.')
fail.close()