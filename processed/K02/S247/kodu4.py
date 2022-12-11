f = open(input("Sisesta lähte faili nimi: "))
g = input("Sisesta siht faili nimi: ")

a = f.read()
b = a.count("Hello")
c = (a.replace("Hello" , "Tere"))
f.close()

f = open(g, "w")
f.write(c)
f.close()

print("Tehti " + str(b) + " asendust.")


