f = open('tere1.txt', encoding='UTF-8')

sisu1 = f.readline()
sisu2 = f.readline()
sisu3 = f.readline()

nimi = input(sisu1)
vanus = input(sisu2)
aadress = input(sisu3)


f = open("tere.txt", "w")
f.write((nimi.replace('Hello', 'Tere')) + "\n")
f.write((vanus.replace('Hello', 'Tere')) + "\n")
f.write((aadress.replace('Hello', 'Tere')) + "\n")
f.close()
f.close()