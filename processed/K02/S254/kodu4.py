fail1 = str(input("Sisestage olemasoleva faili nimi: "))
fail2 = str(input("Sisestage salvestava faili nimi: "))

f = open(fail1)
faili_sisu = f.read()
muudetud_faili_sisu = faili_sisu.replace("Hello", "Tere")
print(faili_sisu.count("Hello"))
f.close()

w = open(fail2, "w")
w.write(muudetud_faili_sisu)
w.close()

