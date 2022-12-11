fail1 = input('Lähtefaili nimi: ')
fail2 = input('Sihtfaili nimi: ')

f1 = open(fail1)
f2 = open(fail2, 'w')

f2.write(f1.read().replace('Hello', 'Tere'))

f1.close()
f2.close()

x = open(fail1, 'r')
asendamised = x.read().count('Hello')

x.close()

print('Tehti' + ' ' + str(asendamised) + ' ' + 'asendust.')