fail1 = input("Lähtefaili nimi: ")
fail2 = input("Sihtfaili nimi: ")

ava1 = open(fail1, "r")
text1 = ava1.read()

print("Tehti "+str(text1.count("Hello"))+" asendamist.")


ava2 = open(fail2, "w")
text2 = text1.replace("Hello", "Tere")
ava2.write(text2)

ava1.close()
ava2.close()