#KN
lahtefail = input("Lähtefaili nimi: ")
sihtfail = input("Sihtfaili nimi: ")

f = open(lahtefail)
x = open(sihtfail, "w")
y = f.read().replace('Hello', 'Tere')
x.write(y)
x.close()
f.close()

f = open(lahtefail)
a = f.read().count('Hello')

print("Tehti " + str(a) + " asendamist.")