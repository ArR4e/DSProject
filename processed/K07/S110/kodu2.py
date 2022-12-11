koju = float(input('Sisesta teepikkus kilomeetrites: '))

f = open('taksohinnad.txt')
sisu = f.readlines()
i = []
nimi = []
n = 0
for rida in sisu:
    rida = rida.strip()
    järjend = rida.split(',')
    #nimi += järjend[0]
    if rida == '':
        break
    hind = float(järjend[1]) + koju * float(järjend[2])
    #hind2 = eelnevalt salvestatud hind
#     if hind < hind2: #kui uus hind on väiksem kui vana, on see odavaima takso nimeks
#         nimi = järjend[0]
#     n += hind
    i += [hind]
    
odavaim = min(i)
print(nimi,odavaim)