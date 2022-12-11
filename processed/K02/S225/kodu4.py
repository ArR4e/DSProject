a = input('Sisestage lähtefaili nimi (lisage ".txt"): ')
b = input('Sisestage sihtfaili nimi (lisage ".txt"): ')

fail_a = open(a, 'r')
x = fail_a.read()

# kogu fail korraga - print(a.read)
# print(fail.readline()) - esimene rida
# teist korda - print(fail.readline()) - teine rida

fail_b = open(b, 'w')

sisu = x.replace('Hello', 'Tere')
fail_b.write(sisu)

loendus = int(sisu.count('Tere'))

fail_a.close()
fail_b.close()

print('Tehti', loendus, 'asendust.')