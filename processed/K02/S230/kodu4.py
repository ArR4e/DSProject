fail=str(input("Sisesta lähtefaili nimi: "))
failvälja=str(input("Sisesta sihtfaili nimi: "))
f=open(fail)
sisu=f.read()
f.close()
a=str(sisu.count("Hello"))


f=open(failvälja, "w")
f.write(sisu.replace("Hello", "Tere"))
f.close()

print("Tehti "+a+" asendamist.")