ing = open('inglise.txt')
sisu = ing.read()

ing.close()

print("Asendusi tehti:", sisu.count("Hallo"))
f = open("eesti.txt", "w")
f.write(sisu.replace("Hallo", "tere"))

f.close()