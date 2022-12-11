fail1 = input("Lähtefaili nimi:")
fail2 = input("Sihtfaili nimi:")
with open (fail1, "r") as f1, open(fail2, "w") as f2:
    for line in f1:
        f2.write(line.replace("Hello","Tere"))


f1 = open(fail1, "r")
date = f1.read()
ilmnes = date.count("Hello")
f1.close()
f2.close()
print("Tehti", ilmnes, "asendamist.")             
