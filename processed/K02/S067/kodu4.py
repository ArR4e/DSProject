def teisenda(fn_1, fn_2):
    f = open(fn_1)
    sisu = f.read()
    print(sisu.count('Hello'))
    uus_sisu = sisu.replace('Hello', 'Tere')
    f.close()
    x = open(fn_2, 'w')
    x.write(uus_sisu)
    x.close()
a = input('Sisesta failinimi:')
b = input('Sisesta uue faili nimi:')
teisenda(a, b)