#küsi failinimesid
algneFail = input('Lähtefaili nimi: ')
uusFail = input('Sihtfaili nimi: ')
#ava olemasolev fail ja asenda sõnad
f = open(algneFail)
sisu = f.read()
asendus = sisu.replace('Hello','Tere')
f.close()
#tee uus fail ja kirjuta asendus sinna sisse
f = open(uusFail, "w")
f.write(asendus)
f.close()
#näita mitu asendust tehti
print(sisu.count('Hello'))