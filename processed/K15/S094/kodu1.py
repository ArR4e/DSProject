import re

fail = open('aadressid.txt', encoding='utf-8')
for rida in fail:
    if (re.search("ut.ee", rida)) != None:
        # nüüd vaja ainult kasutajanimi saada peale '~' märki.
        kasutajanimi = re.search('~(\w+)', rida)
        if kasutajanimi != None:                    
            print(kasutajanimi.group(1))



fail.close()