text1 = input("Lähtefaili nimi: ")
text2 = input("Sihtfaili nimi: ")
f = open(text1, encoding="cp1257")
fail1_sisu = f.read()
hello_count = fail1_sisu.count("Hello")
print("Tehti ",hello_count," asendamist")
replaced_text = fail1_sisu.replace("Hello", "Tere")
m = open(text2, "w")
m.write(replaced_text)
m.close()


