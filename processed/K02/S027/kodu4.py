f = open(input('Sisestage faili nimi, mida tõlkida: '))
sisu = f.read()
q = sisu.count('hello')
f.close()

g = open(input('Andke tõlgitud failile nimi: '), 'w')
g.write(sisu.replace("hello", "tere"))
g.close()
print('tehti ' + str(q) + ' asendust')