lahtefail = input("Sisestage lähtefaili nimi: ")
sihtfail = input("Sisestage sihtfaili nimi: ")

l_fail = open(lahtefail, 'r', encoding = "UTF-8")
s_fail = open(sihtfail, 'w', encoding = "UTF-8")
asendused = 0

for rida in l_fail:
    asendused = asendused + rida.count('Hello')
    s_fail.write(str(rida).replace('Hello', 'Tere'))

print("Tehti " + str(asendused) + " asendamist.")

l_fail.close()
s_fail.close()