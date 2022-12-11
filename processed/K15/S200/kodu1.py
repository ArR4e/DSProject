import re
f = 'aadressid.txt'
with open(f) as fail:
    for rida in fail:
        rida = str(rida.split())
        if re.search("http://www.ut.ee/~(\w+)/",rida):
            kasutaja = re.search(r'http://www.ut.ee/~(\w+)/',rida)
            print(kasutaja.group(1))
        
    