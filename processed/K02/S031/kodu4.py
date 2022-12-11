kust = input('Sisu tuleb sellest failist: ')
kuhu = input('Sisu kirjutatakse sellesse faili: ')

a = open(kust)
b = open(kuhu,'w')
kogus = 0
for rida in a:
    kogus += rida.count('Hello')
    tere = rida.replace('Hello','Tere')
    b.write(tere)
print(kogus)
a.close()
b.close()