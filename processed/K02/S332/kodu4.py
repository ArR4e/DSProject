failinimi = input("Kirjuta failinimi mida teha lahti: ")
sihtfail = input("Uue faili nimi: ")
f = open(failinimi)
text = f.read().replace("Hello","Tere")
teisend = (text).count("Tere")

print(f"Faili {sihtfail} sisu: ")
print(text)
print(f"Tehti {teisend} asendamist.")

