l_fail = input("Sisestage lähtefaili nimi: ")
s_fail = input("Sisestage sihtfaili nimi: ")
f1 = open(l_fail, "r", encoding="UTF-8")
f2 = open(s_fail, "a+", encoding="UTF-8")
x = 0
for rida in f1:
    x += rida.count("Hello")
    f2.write(rida.replace("Hello", "Tere"))
f1.close()
f2.close()
print("Tehti " + str(x) + " vahetust tekstis")