f = open('taksohinnad.txt', encoding = 'UTF-8')

tee_pikkus = float(input('Sisesta tee pikkus kilomeetrited: '))
järjend_nimed = []
järjend_hinnad = []
kõige_odavam_firma = ''

for rida in f:
    rida_ok = rida.strip().split(',')
    firma = rida_ok[0]
    alustamistasu = float(rida_ok[1])
    km_hind = float(rida_ok[2])
    sõidu_hind = alustamistasu + km_hind * tee_pikkus
    järjend_nimed += firma.split(',')
    järjend_hinnad.append(sõidu_hind)
    kõige_odavam_hind = min(järjend_hinnad)
    indeks = järjend_hinnad.index(kõige_odavam_hind)
    kõige_odavam_firma = järjend_nimed[indeks]

f.close()

if tee_pikkus == float(0):
    print('Koju ei lähe?')
elif kõige_odavam_firma != '':
    print('Kõige odavam on', kõige_odavam_firma)
else:
    print('Info taksofirmade kohta puudub.')