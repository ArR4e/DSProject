failin=input("Palun sisestage lähtefaili nimi koos laiendiga: ")
sihtfailin=input("Palun sisestage sihtfaili nimi koos laiendiga: ")
lf=open(failin,'r' )
#siia vist kuhu salvestab
vahetus=(lf.read())
uus=vahetus.replace('Hello', 'Tere')
kaks=vahetus.count('Hello')

lf.close()

muutuja2=open(sihtfailin, 'w')
muutuja2.write(str(uus))
muutuja2.close()

print(kaks)
