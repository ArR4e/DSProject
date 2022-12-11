fail1 = input('Lähtefaili nimi: ')
fail1 =str(fail1)
fail2 = input('Sihtfaili nimi: ')
fail2 =str(fail2)

f = open(fail1)
faili_sisu = f.read()
print(faili_sisu)
f.close()

f = open(fail2, "w")
f.write(faili_sisu.replace("Hello","Tere"))
f.close()

f = open(fail2)
faili_sisu = f.read()
print(faili_sisu)
f.close()

f = open(fail2)
faili_sisu = f.read()
print(faili_sisu.count('Tere'))
f.close()