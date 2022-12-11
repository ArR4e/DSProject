import re
with open('aadressid.txt', encoding='UTF-8') as f:
    for rida in f:
        rida = rida.strip()
        if re.match('http://www.ut.ee/~(\w+)', rida):
            rida = re.match('http://www.ut.ee/~(\w+)', rida)
            print(rida.group(1))