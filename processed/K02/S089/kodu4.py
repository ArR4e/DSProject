fail1 = input('Lähtefaili nimi: ')
fail2 = input('Sihtfaili nimi: ')
f = open(fail1)
faili_sisu = f.read()
kogus = faili_sisu.count('Hello')
tõlgitud = faili_sisu.replace('Hello', 'Tere')
print('Tehti ' + str(kogus) + ' asendamist. \n')
f.close()
f1 = open(fail2, 'w')
f1.write(tõlgitud)
f1.close()
print('Faili ' + str(fail2) + ' sisu: \n')
print(tõlgitud)