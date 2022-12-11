esimene = input("Lähtefaili nimi: ") 
teine = input("Sihtfaili nimi: ")

fa = open(esimene , "r" , encoding="UTF-8")
data = fa.read()
c = data.count("Hello")
x = data.replace("Hello", "Tere")
print("Tehti " + str(c) + " asendamist. ")

f = open(teine, "w")

f.write(x)
f.close()