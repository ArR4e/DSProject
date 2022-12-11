import re

f = open('aadressid.txt', 'r', encoding = 'utf-8')
print('Kasutajanimed on:')
for rida in f:
    rida = rida.strip()
    kasutajanimi_kontroll = re.search("www.ut.ee/~[a-zA-Z0-9]+/", rida) # Kontrollib, kas "www.ut.ee/~<nimi>/" on olemas
    if kasutajanimi_kontroll != None:
        kasutajanimi_olemas = kasutajanimi_kontroll.group().replace('www.ut.ee/~', '').strip('/') # Jätab järgi ainult vaste
        print(kasutajanimi_olemas)
    