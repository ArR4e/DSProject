#Masintõlge
#For tsükli idee tuli "Tarbijast loojaks" kursuselt

fail1 = input("Sisesta esimese faili nimi:")
fail2 = input("Sisesta teise faili nimi:")

fail_avamine = open(fail1, encoding="UTF-8")
fail_loomine = open(fail2, "w", encoding="UTF-8")

algfail = []
i = 1
asendused = 0

for rida in fail_avamine:
    algfail.append(rida)
    asendused = asendused + algfail[i-1].count("Hello")
    fail_loomine.write(algfail[i-1].replace("Hello", "Tere"))
    i+=1
    
fail_avamine.close()
fail_loomine.close()

print(asendused)
