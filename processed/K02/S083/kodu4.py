lähtefail = input('Lähtefaili nimi: ')
sihtfail = input('Sihtfaili nimi: ')
f1 = open(lähtefail)
f1_asendus = f1.read().replace('Hello', 'Tere')

f2 = open(sihtfail, 'w+')
f2_asendus = f2.write(f1_asendus)
f1.close()
f2.close()

asenduste_arv = open(sihtfail)
print('Sooritati', asenduste_arv.read().count('Tere'), 'asendamist!')
asenduste_arv.close()