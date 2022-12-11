fail1 = input("Sisestage inglisekeelne failinimi: ")
fail2 = input("Sisestage eestikeelne failinimi: ")

f = open(fail1)
faili_sisu = f.read().replace('Hello','Tere')

f_uus = open(fail2, "w")
f_uus.write(faili_sisu)

asendamised = faili_sisu.count('Tere')
print(asendamised)

f.close()
f_uus.close()