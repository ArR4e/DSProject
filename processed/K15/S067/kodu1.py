import re

with open('aadressid.txt', encoding='utf-8') as f:
    nimed = []
    while True:
        nimi = []
        g = f.readline().strip()
        if g == '':
            f.close()
            break
        if re.match('http://www.ut.ee/', g):
            if re.search("(/~.){1}", g):
                rida = g.split('/~')
                for täht in rida[1]:
                    if täht != '/':
                        nimi.append(täht)
                    else:
                        break
                nimed.append(''.join(nimi))
            else:
                continue
        else:
            continue
    f.close()
if len(nimed) != 0:
    print('Kasutajanimed on: ')
    print('\n'.join(nimed))