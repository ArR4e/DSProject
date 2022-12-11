fail = open('inglise.txt')
sisu = fail.read()
fail.close()
uus_sisu = sisu.replace('Hello' , 'Tere')

uusfail = open('eesti.txt' , 'w')
uusfail.write(uus_sisu)
uusfail.close()
print(uus_sisu)

print(sisu.count('Hello'))
