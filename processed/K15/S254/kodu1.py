import re

fail = open('aadressid.txt', encoding='UTF-8')
for rida in fail:
    kasutaja = re.search('http://www.ut.ee/~(\w*)/', rida)
    if kasutaja:
        print(kasutaja.group(1))
    else:
        continue
fail.close()