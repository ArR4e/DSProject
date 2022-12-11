f1 = input('Sisestage lähtefaili nimi: ')
f2 = input('Sisestage sihtfaili nimi: ')

f1_ava = open(f1)
f1_loe = open(f1).read().count('Tere')
f1_asenda = open(f1).read().replace('Hello', 'Tere')

f2_ava = open(f2, 'w+')
f1_kirjuta = f2_ava.write(f1_asenda)

f1_ava.close()
f2_ava.close()

tulemus = open(f2)
print('\n' + '\n' + 'Lähtefail: ' + f1 + '\n' + 'Sihtfail: ' + f2)
print('Sooritati ' + str(tulemus.read().count('Tere') - f1_loe) + ' asendamist.')
tulemus.close()