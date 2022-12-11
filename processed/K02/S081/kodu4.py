Lfail = input('Lähtefaili nimi: ')
Sfail = input('Sihtfaili nimi: ')

a=0

fail1 = open(Lfail, encoding='UTF-8')
fail2 = open(Sfail,'w')
for rida in fail1:
    a += rida.count('Hello')
    rida = rida.replace('Hello', 'Tere')
    fail2.write(rida)

print('Tehti ' + str(a) + ' asendamist.')
fail1.close()
fail2.close()