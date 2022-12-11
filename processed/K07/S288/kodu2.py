from re import sub

with open('taksohinnad.txt', encoding = 'UTF-8') as f:
    x = f.readlines()

teepikkus = float(input('Sisestage tee pikkus kilomeetrites: '))

i = 0
taksod = []
hinnad = []

while i < len(x):
    if len(x) == 0:
        break
    takso_nimi = sub('[^a-zA-ZõÕäÄöÖüÜ ]', '', x[i])
    takso_kohandatud = sub('[^0-9.,]', '', x[i])
    takso_list = sub('[^0-9.]', ' ',takso_kohandatud[1:]).split()
    takso_hind = float(takso_list[0]) + float(takso_list[1]) * teepikkus
    taksod.append(takso_nimi)
    hinnad.append(takso_hind)
    i += 1

if len(x) != 0:
    parim_takso_hind = min(hinnad)
    parim_takso_indeks = hinnad.index(parim_takso_hind)
    parim_takso_nimi = taksod[parim_takso_indeks]
    print('Kõige odavam on ' + parim_takso_nimi + '.')
else:
    print('Failis puuduv vajalik sisu.')