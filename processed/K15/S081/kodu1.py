fail = open('aadressid.txt', encoding='utf-8')
print('Kasutaja nimed on: ')
for rida in fail:
    if 'http://www.ut.ee/~' in rida:
        link = rida.strip('\n')
        äge = rida.replace('http://www.ut.ee/~','')
        isik = ''
        for el in äge:
            if el != '/':
                isik += el
            else:
                break
        print(isik) 