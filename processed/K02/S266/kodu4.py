fail1 = input("Sisestage lähtefaili nimi: ")
fail2 = input("Sisestage sihtfaili nimi: ")

f1_sisu = open(fail1, encoding= 'UTF-8')
f2_sisu = open(fail2, "w", encoding= 'UTF-8')

asendamised = 0
for rida in f1_sisu:
    f2_sisu.write(rida.replace("Hello", "Tere"))
    asendamised += rida.count("Hello")
    
print("Asendamisi tehti ", asendamised)

f1_sisu.close()
f2_sisu.close()
