fail1 = input('Sisesta esimese faili nimi: ')
fail2 = input('Sisesta teise faili nimi: ')
i = open(fail1).read()
open(fail2, 'w').write(i.replace('Hello', 'Tere'))
print('Tehti ' + str(i.count('Hello')) + ' asendamist.')