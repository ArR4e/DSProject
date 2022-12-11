x = input("Sisesta failinimi: ")
y = input("Sisesta uus failinimi: ")

f = open(x)

faili_sisu = f.read()
s = faili_sisu.count('Hello') 
f.close()

f = open(y, "w")

f.write(faili_sisu.replace('Hello', 'Tere'))    

print("Tehtud on: " + str(s) + " " + "muudatust")

f.close()