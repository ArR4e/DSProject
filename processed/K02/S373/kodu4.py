lahtefail = input("Lähtefaili nimi: ")
sihtfail = input("Sihtfaili nimi: ")
f1 = open(lahtefail, "r", encoding="UTF-8")
f2 = open(sihtfail, "a+", encoding="UTF-8")
n = 0
for rida in f1:
    n += rida.count("Hello")
    f2.write(rida.replace("Hello", "Tere"))
f1.close()
f2.close()                  
print("Tehti " + str(n) + " vahetust tekstis.")



