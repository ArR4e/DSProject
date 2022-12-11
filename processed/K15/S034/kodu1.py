import re
nimi = ""
kas_esimene = 0
f = open('aadressid.txt')
for rida in f:    
    aadress = rida.strip()
    if re.match('http://www.ut.ee/~',aadress):
        
        palju = len('http://www.ut.ee/~')
        for täht in aadress[palju:]:
            if täht.isalnum():
                nimi += täht
            else:
                break
        if kas_esimene == 0:
            kas_esimene +=1
            print('Kasutajanimed on: ')
        print(nimi)
        nimi = ""

f.close
