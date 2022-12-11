ans1 = input("Lähtefaili nimi: ")
ans2 = input("Sihtfaili nimi: ")

# Encoding igaks juhuks kui fail sisaldab täpitähti
f1 = open(ans1, encoding="UTF-8")
f2 = open(ans2, "a", encoding="UTF-8")

sisu = f1.read()
asenduste_arv = sisu.count("Hello")
uus_sisu = sisu.replace("Hello", "Tere")
print("Tehti " + str(asenduste_arv) + " asendamist.")

f2.write(uus_sisu)

f1.close()
f2.close()