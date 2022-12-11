fIn = open(input("Sisesta olemasoleva faili nimi: "), "r")
fOut = open(input("Sisesta väljundfaili nimi: "), "w+")

i = 0
for line in fIn:
    i += line.count('Hello')
    fOut.write(line.replace('Hello', 'Tere'))

print("Tehti " + str(i) + " asendamist.")
fIn.close()
fOut.close()