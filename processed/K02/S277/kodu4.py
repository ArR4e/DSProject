f = open(input('Sisestage esialgse faili nimi: '))
f2 = open(input('Sisestage teise faili nimi: '), 'w')

fail1 = f.read()
print(fail1.count('Hello'))

asendused = fail1.replace('Hello', 'Tere')
f2.write(asendused)

f.close()
f2.close()
