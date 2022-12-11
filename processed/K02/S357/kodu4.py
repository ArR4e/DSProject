filename = input("Lähtefaili nimi: ")
sihtfail = input("Sihtfaili nimi: ")

f = open(filename, "r")
text = f.read()

x = text.replace("Hello", "Tere")

print("Tehtud asendusi kokku", (text.count("Hello")))

z = open(sihtfail, "w")
z.write(x) 
z.close()
f.close()