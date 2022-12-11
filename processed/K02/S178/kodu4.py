
inglise= input('Siseta failinimi  ')
eesti= input('Kuhu tahad tõlkida  ')
f = open(inglise)
faili_sisu = f.read()
a = faili_sisu.replace('Hello' , 'Tere').replace('hello' , 'tere')
e = open(eesti , 'a')
e.write(a)

k = faili_sisu.count('Hello')
g = faili_sisu.count('hello')
print('Asendamisi tehti: ')
print(k + g)
