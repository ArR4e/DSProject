f1 = input('Lähtefaili nimi: ')
f2 = input('Sisefaili nimi: ')

inglise = open(f1)
eesti = open(f2, 'w')
asendus = 0

a = inglise.read()
asendus = a.count('Hello')
asendatud = a.replace('Hello', 'Tere')
eesti.write(asendatud)

print('Tehti ' + str(asendus) + ' asendamist.')

inglise.close()
eesti.close()