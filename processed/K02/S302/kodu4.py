lahtefail = input("Lähtefaili nimi: ")
sihtfail = input("Sihtfaili nimi: ")

f = open(lahtefail, "r", encoding="UTF-8")
ff = open(sihtfail, "w", encoding="UTF-8")

teresid = 0
for rida in f:
    ff.write(f.read().replace("Hello", "Tere"))
    teresid += 1
    
f.close()
ff.close()

print("Tehti " + str(teresid) + "asendamist." )