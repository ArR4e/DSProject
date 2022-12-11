import re
fail = open('aadressid.txt')

print('Kasutajanimed on:')
for rida in fail:
    if re.match('http://www.ut.ee/~', rida):
        algus = 'http://www.ut.ee/~'
        lõpp = '/'
        print((rida.split(algus))[1].split(lõpp)[0])
#         sõne = re.search("http://www.ut.ee/~(.*)/", rida)
#         print(sõne.group(1))
        
fail.close()