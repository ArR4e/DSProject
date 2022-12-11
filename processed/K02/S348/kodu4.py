Lähtefail = input("Palun sisestage lähtefaili nimi: ")
Sihtfail = input("Palun sisestage sihtfaili nimi: ")
f1 = open(Lähtefail)
f2 = open (Sihtfail , "w")
c = 0
for line in f1:
    f2.write(line.replace("Hello" , "Tere"))
    c += line.count("Hello")
f1.close()
f2.close()
print("Teisendusi tehti",c,"korda")


