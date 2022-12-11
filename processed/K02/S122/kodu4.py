fail_tekst = input("Palun sisesta lähtefaili nimi: ")
fail_muu = input("Palun sisesta sihtfaili nimi: ")

algfail = open(fail_tekst, "r")
    
sisu = algfail.read()

counter = sisu.count("Hello")

muudetudsisu = sisu.replace("Hello", "Tere")

algfail.close()

muudetudfail = open(fail_muu, "w")

muudetudfail.write(muudetudsisu)

muudetudfail.close()

print("Tehtud asendusi: " + str(counter))