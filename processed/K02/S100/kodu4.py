f1 = open(input("Lähtefaili nimi: "), "r")
f2 = open(input("Väljundifaili nimi: "), "w")

text = f1.read()

muutumised = text.count("Hello")
text = text.replace("Hello", "Tere")

f2.write(text)
f1.close()
f2.close()

print(f"Tehti {muutumised} asendamist.")