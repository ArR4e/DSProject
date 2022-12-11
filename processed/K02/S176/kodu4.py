a_fail = input("Sisesta algse faili nimi: ")
b_fail = input("Sisesta sihtfaili nimi: ")

f = open(a_fail, encoding = 'UTF-8')
g = open(b_fail, 'w', encoding = 'UTF-8')

sisu = f.read()
vahetused = sisu.count('Hello')
g.write(sisu.replace('Hello', 'Tere'))
f.close()
g.close()
print("Tehti " + str(vahetused) + " vahetust")