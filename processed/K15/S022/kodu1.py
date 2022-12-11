import re

fail = open('aadressid.txt','r')
print('Kasutajanimed on: ')
for rida in fail:
    try:
        rida = rida.strip()
        if rida[0] == 'h':
            rida = rida.split('/')
            ut = rida[2]
            if re.search('www.ut.ee', ut):
                if re.search('~.*',rida[3]):
                    nimi = rida[3]
                    nimi = nimi[1:]
                    print(nimi)
    except:
        continue
fail.close()