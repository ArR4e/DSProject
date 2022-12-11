fail = input('Sisesta failinimi: ')
f = open(fail)
for rida in f:
    if 'http://www.ut.ee/' in rida:
        vahe = rida.split('http://www.ut.ee/~')
        osak = vahe[1]
        vahe2 = osak.split('/')
        nimi = vahe2[0]
        print(nimi)


f.close()