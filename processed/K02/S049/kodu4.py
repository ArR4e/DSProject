fail_a = input("Sisestage lähtefaili nimi: ")
fail_b = input("Sisestage sihtfaili nimi: ")
f1 = open(fail_a, "r")
a = f1.read()
a.count("Hello")
f2 = open(fail_b, "w")
f2.write(a.replace("Hello", "Tere"))
f1.close()
f2.close()
print(a.count("Hello"))