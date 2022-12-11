vana_fail = input("Palun sisesta töödeldava faili nimi: ")
uus_fail = input("Palun sisesta uue faili nimi: ")

f = open(vana_fail)
tekst = f.read()
f.close()

print("Sooritati " + str(tekst.count("Hello")) + " asendust.")

n = open(uus_fail, "w")
n.write(tekst.replace("Hello", "Tere"))
n.close()