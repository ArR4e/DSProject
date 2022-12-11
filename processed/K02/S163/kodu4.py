lähtefail = input('Lähtefaili nimi: ')
sihtfail = input('Sihtfaili nimi: ')

f1 = open(lähtefail, 'r')
f2 = open(sihtfail, 'a')

asendused = 0

for rida in f1:
    asendused += rida.count('Hello')
    rida = rida.replace('Hello', 'Tere')
    f2.write(rida)
    
f1.close()
f2.close()

print(asendused)