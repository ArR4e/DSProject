fail1 = input("Sisestage lähtefaili nimi:")
fail2 = input("Sisestage sihtfaili nimi:")

f = open(fail1,"r")
f2 = open(fail2,"x")

sisu = f.read()
x = sisu.count("Hello")

sisu = sisu.replace("Hello", "Tere")

f2.write(sisu)

f.close()
f2.close()

print("Tehti "+str(x)+" asendamist.")

